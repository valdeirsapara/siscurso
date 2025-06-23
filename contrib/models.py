from django.db import models
from django.contrib.auth.models import User
from curso.models import Curso
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


class Carrinho(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='carrinho')
    cursos = models.ManyToManyField(Curso, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.aluno.nome_completo} - Carrinho ({self.data_criacao})"
    
    @property
    def total_cursos(self):
        return self.cursos.count()

    def adicionar_curso(self, curso):
        """
        Adiciona um curso ao carrinho do aluno.
        """
        if not isinstance(curso, Curso):
            raise ValueError("O objeto deve ser uma instância de Curso.")
        
        self.cursos.add(curso)
        self.save()

    def remover_curso(self, curso):
        """
        Remove um curso do carrinho do aluno.
        """
        if not isinstance(curso, Curso):
            raise ValueError("O objeto deve ser uma instância de Curso.")
        
        self.cursos.remove(curso)
        self.save()
    
    def limpar_carrinho(self):
        """
        Limpa todos os cursos do carrinho do aluno.
        """
        self.cursos.clear()
        self.save()


class Ordem(models.Model):
    PEDENTE = 'pendente'
    PAGO = 'pago'
    CANCELADO = 'cancelado'
    EM_PROCESSAMENTO = 'em_processamento'

    STATUS_CHOICES = [
        (PEDENTE, 'Pendente'),
        (PAGO, 'Pago'),
        (CANCELADO, 'Cancelado'),
    ]

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='ordens')
    curso = models.ManyToManyField(Curso, blank=True)
    data_pagamento = models.DateTimeField(auto_now_add=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PEDENTE)

    def __str__(self):
        return f"{self.aluno.nome_completo} - {self.curso.name} - {self.status}"
    
    def pagar(self):
        """
        Marca a ordem como paga.
        """
        self.status = 'pago'
        self.save()
    
    def startar_pagamento(self):
        """
        Inicia o processo de pagamento.
        """
        if self.status != self.PEDENTE:
            raise ValueError("A ordem já foi paga ou cancelada.")
        
        self.status = self.EM_PROCESSAMENTO
        self.save()
        self.pagar()
        return self.status


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