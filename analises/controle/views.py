from django.shortcuts import render
from .models import Projeto, Amostra, Analise

# Create your views here.


def index(request):
    projetos = Projeto.objects.all()
    return render(request, "index.html", {"projetos": projetos})

def projeto(request, id):
    analises = Analise.objects.all()
    return render(request, "projeto.html", {"analises": analises})

def analise(request, id):
    amostras = Amostra.objects.all()
    return render(request, "amostra.html", {"amostras": amostras})