from django.db import models
from django.contrib.auth.models import User
    

class tipo_de_automação(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(verbose_name='Descrição')

    def __str__(self):
        return self.nome


class pedidos(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    tipo = models.ForeignKey(tipo_de_automação, null=True, on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.mensagem + " - Criado em: " + self.criado_em.strftime("%d/%m/%Y %H:%M")


