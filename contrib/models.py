from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='aluno')

    @property
    def nome_completo(self):
        if not self.user:
            return "Sem usuário"
        nome = self.user.get_full_name()
        if nome and nome.strip():
            return nome
        return self.user.username or f"Usuário {self.user.pk}"
    
    def __str__(self):
        if not self.user:
            return "Aluno sem usuário"
        
        nome = self.user.get_full_name()
        if nome and nome.strip():
            return nome
        
        username = self.user.username
        if username and username.strip():
            return username
            
        return "Usuário sem nome"
    
class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='professor')
    
    @property
    def nome_completo(self):
        if not self.user:
            return "Sem usuário"
        nome = self.user.get_full_name()
        if nome and nome.strip():
            return nome
        return self.user.username or f"Usuário {self.user.pk}"


    def __str__(self):
        if not self.user:
            return "Professor sem usuário"
        
        nome = self.user.get_full_name()
        if nome and nome.strip():
            return nome
        
        username = self.user.username
        if username and username.strip():
            return username
            
        return "Usuário sem nome"


# Signals para criar Professor e Aluno automaticamente
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Quando um usuário é criado, cria automaticamente um perfil de Professor e Aluno associado
    """
    if created:
        # Cria um perfil de Professor para o usuário
        Professor.objects.create(user=instance)
        # Cria um perfil de Aluno para o usuário
        Aluno.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Quando um usuário é atualizado, atualiza também os perfis associados
    """
    # Garante que o perfil de Professor existe
    if hasattr(instance, 'professor'):
        instance.professor.save()
    else:
        Professor.objects.create(user=instance)
    
    # Garante que o perfil de Aluno existe
    if hasattr(instance, 'aluno'):
        instance.aluno.save()
    else:
        Aluno.objects.create(user=instance) 