from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Amostra, Projeto, Analise, Usuario

# Register your models here.
class BaseAdmin(admin.ModelAdmin):
    """Classe base para definir automaticamente os usuários de criação e atualização"""
    exclude = ("criado_por", "atualizado_por")  # Oculta os campos no formulário

    def save_model(self, request, obj, form, change):
        """Define automaticamente os campos de usuário ao salvar"""
        if not obj.pk:  # Se for um novo objeto
            obj.criado_por = request.user
        obj.atualizado_por = request.user  # Sempre atualizado pelo usuário atual
        super().save_model(request, obj, form, change)


# Administração do modelo Projeto
@admin.register(Projeto)
class ProjetoAdmin(BaseAdmin):
    list_display = ("nome", "ativo", "data", "criado_por", "atualizado_por")

# Administração do modelo Analise
@admin.register(Analise)
class AnaliseAdmin(BaseAdmin):
    list_display = ("nome", "projeto", "criado_por", "atualizado_por")

# Administração do modelo Amostra
@admin.register(Amostra)
class AmostraAdmin(BaseAdmin):
    list_display = ("nome", "analise", "peso_cap_vazia", "amostra_inicial", "peso_final", "umidade", "criado_por", "atualizado_por")


class CustomUserAdmin(UserAdmin):
    model = Usuario
    fieldsets = UserAdmin.fieldsets + (
        ("Permissões Personalizadas", {"fields": ("administrador",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Permissões Personalizadas", {"fields": ("administrador",)}),
    )

admin.site.register(Usuario, CustomUserAdmin)