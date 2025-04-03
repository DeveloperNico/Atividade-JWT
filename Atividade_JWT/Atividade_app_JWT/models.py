from django.db import models
from django.contrib.auth.models import AbstractUser

class Pessoa(AbstractUser):
    biografia = models.TextField(null=True, blank=True)
    idade = models.IntegerField(null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    endereco = models.CharField(max_length=255, null=True, blank=True)
    escolaridade = models.CharField(max_length=50, null=True, blank=True)
    qte_animais = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username    
