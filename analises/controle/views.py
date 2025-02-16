from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Projeto, Amostra, Analise

# Create your views here.

@login_required
def index(request):
    projetos = Projeto.objects.all()
    return render(request, "index.html", {"projetos": projetos})

@login_required
def projeto(request, id):
    analises = Analise.objects.all()
    return render(request, "projeto.html", {"analises": analises})

@login_required
def analise(request, id):
    amostras = Amostra.objects.all()
    return render(request, "amostra.html", {"amostras": amostras})