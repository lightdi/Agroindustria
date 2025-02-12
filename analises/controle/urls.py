from .views import index, analise, projeto
from django.urls import path

urlpatterns =[
    path('', index, name="index"),
    path('projeto/<int:id>/', projeto, name="analise" ),
    path('analise/<int:id>/', analise, name="amostras")
]