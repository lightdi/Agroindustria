from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Projeto, Amostra, Analise
from .forms import ProjetoForm

# Create your views here.

@login_required
def index(request):
    # Se o usuário for administrador, ele pode ver todos os projetos
    if request.user.administrador:
        projetos = Projeto.objects.all()
    else:
        # Caso contrário, busca projetos onde o usuário é o criador ou onde ele tem permissão de visualização
        projetos = Projeto.objects.filter(
            criado_por=request.user
        ) | Projeto.objects.filter(
            permissaoprojeto__usuario=request.user, 
            permissaoprojeto__pode_visualizar=True
        )

    return render(request, "index.html", {"projetos": projetos})

@login_required
def criar_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            # Passa o usuário logado para o formulário ao salvar
            form.save(usuario=request.user)  # O usuário logado é passado aqui
            return redirect('index')  # Redireciona para a lista de projetos ou outro local
    else:
        form = ProjetoForm()

    return render(request, 'criar_projeto.html', {'form': form})

@login_required
def editar_projeto(request, id):
    projeto = get_object_or_404(Projeto, id=id)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            # Atribui o usuário logado ao campo 'alterado_por'
            projeto = form.save(commit=False)  # Não salva automaticamente
            projeto.alterado_por = request.user  # Atribui o usuário logado
            projeto.save()  # Salva o projeto com a alteração do usuário
            return redirect('index')  # Redireciona para a lista de projetos
    else:
        print(projeto.data)
        form = ProjetoForm(instance=projeto)
        form.fields['data'].initial = '2020-11-11'#projeto.data.strftime('%Y-%m-%d')
        print(form.fields['data'].initial)

    return render(request, 'editar_projeto.html', {'form': form, 'projeto': projeto})

@login_required
def projeto(request, id):
    analises = Analise.objects.all()
    return render(request, "projeto.html", {"analises": analises})

@login_required
def analise(request, id):
    amostras = Amostra.objects.all()
    return render(request, "amostra.html", {"amostras": amostras})