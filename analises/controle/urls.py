from .views import index, analise, projeto, criar_projeto, editar_projeto
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('', index, name="index"),
    path('projeto/<int:id>/', projeto, name="analise" ),
    path('adicionar_projeto/', criar_projeto, name="adicionar_projeto" ),
    path('editar_projeto/<int:id>/', editar_projeto, name="editar_projeto" ),
    
    path('analise/<int:id>/', analise, name="amostras"),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
]