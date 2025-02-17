from django import forms
from .models import Projeto
from django.utils import timezone

class CustomDateInput(forms.DateInput):
    input_type = 'date'


    def render(self, name, value, attrs=None, renderer=None):
        if value:
            # Garantir que o valor esteja no formato 'YYYY-MM-DD'
            value = value.strftime('%Y-%m-%d')  # Formato correto para input[type="date"]
        return super().render(name, value, attrs, renderer)
    

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao', 'data', 'ativo']  # Campos que você quer permitir que o usuário preencha
    
    # Adicionando classes de Bootstrap aos campos do formulário
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    #initial=timezone.localtime(timezone.now()).date().strftime('%Y-%m-%d'),
    data = forms.DateField(  initial=timezone.now().date(), widget=CustomDateInput(attrs={'class': 'form-control', 'type': 'date'}))
    ativo = forms.BooleanField(initial=True, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    


    
    def save(self, *args, **kwargs):
        # Preenche o campo 'criado_por' com o usuário logado antes de salvar
        usuario = kwargs.pop('usuario', None)  # Pega o usuário passado como argumento
        instance = super(ProjetoForm, self).save(*args, **kwargs)  # Salva o projeto
        if usuario:
            instance.criado_por = usuario  # Associa o usuário ao campo 'criado_por'
            instance.save()  # Salva novamente com o campo 'criado_por' preenchido
        return instance
