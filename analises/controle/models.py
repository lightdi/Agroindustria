from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#Usuários 
class Usuario(AbstractUser):
    administrador = models.BooleanField(default=False, verbose_name='Administrador')



#Criação da tabela dos projetos
class Projeto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255, null=False)
    #analise = models.ForeignKey("Analise", on_delete=models.CASCADE, related_name="analise",  blank=True)
    descricao = models.TextField(max_length=500, null=False)
    ativo = models.BooleanField(default=True, null=False)
    data = models.DateField(null=False)
    atualizado = models.DateTimeField(auto_now=True)
    
    #Usuário responsável pelo projeto
    criado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name="projetos_criados")
    atualizado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name="projetos_atualizados")
    def __str__(self):
        return self.nome 


#Criação da tabela das analises 
class Analise(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255, null=False)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    #Usuário responsável pela análise
    criado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name="analises_criados")
    atualizado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name="analises_atualizados")
    #amostra = models.ForeignKey(Amostra, on_delete=models.CASCADE, related_name="amostra")
    def __str__(self):
        return self.nome
    


#Criação da tabela das amostras
class Amostra(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255, null=False)
    analise = models.ForeignKey("Analise", on_delete=models.CASCADE)
    peso_cap_vazia = models.FloatField()
    amostra_inicial = models.FloatField()
    peso_final = models.FloatField()
    umidade = models.FloatField()

    #Usuário responsável pela amostra
    criado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name="amostras_criados")
    atualizado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name="amostras_atualizados")
    def um(self):
        peso_inicial = self.peso_cap_vazia + self.amostra_inicial
        umidade = ((peso_inicial - self.peso_final)/ self.amostra_inicial) * 100
        return round(umidade,2)
    
    def __str__(self):
        return self.nome
    

