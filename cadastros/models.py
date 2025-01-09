from django.db import models
from django.utils import timezone

class Usuario(models.Model):

    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    

    data_criacao = models.DateTimeField(default=timezone.now)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def data_criacao_formatada(self):
        return self.data_criacao.astimezone(timezone.get_default_timezone()).strftime(
            "%d/%m %H:%M"
        )

    def data_atualizacao_formatada(self):
        return self.data_atualizacao.astimezone(
            timezone.get_default_timezone()
        ).strftime("%d/%m %H:%M")

    def __str__(self):
        return f"{self.nome} - Criado em {self.data_criacao_formatada()} - Atualizado {self.data_atualizacao_formatada()}"
