from django.db import models
from django.contrib.auth.models import User, BaseUserManager

class Pessoa(models.Model):
    login = models.CharField(max_length=20)
    senha = models.CharField(max_length=20, null=False, blank=True,)
    data_nascimento = models.DateField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self) -> str:
        return self.login



