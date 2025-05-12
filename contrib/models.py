from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='aluno')

    @property
    def nome_completo(self):
        return self.user.get_full_name()
    
    def __str__(self):
        if self.user:
            return self.user.get_full_name() or self.user.username
        return "Professor sem usuário"
    
class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='professor')
    
    @property
    def nome_completo(self):
        return self.user.get_full_name()


    def __str__(self):
        if self.user:
            return self.user.get_full_name() or self.user.username
        return "Professor sem usuário"

