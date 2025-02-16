from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Amostra, Projeto, Analise, Usuario

# Register your models here.


admin.site.register(Amostra)

admin.site.register(Projeto)

admin.site.register(Analise)


class CustomUserAdmin(UserAdmin):
    model = Usuario
    fieldsets = UserAdmin.fieldsets + (
        ("Permissões Personalizadas", {"fields": ("administrador",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Permissões Personalizadas", {"fields": ("administrador",)}),
    )

admin.site.register(Usuario, CustomUserAdmin)