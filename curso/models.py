# django
from django.db import models

# third parties
from polymorphic.models import PolymorphicModel

# local 
from core.models import AbstractMixin


# Create your models here.
class Curso(PolymorphicModel, AbstractMixin):
    name = models.CharField(max_length=255) # campo obrigatorio
    description = models.TextField()
    duracao = models.PositiveIntegerField()  # duração em horas
    # modulos = models.ManyToManyField('Modulo', related_name='cursos')
    alunos = models.ManyToManyField("contrib.Aluno", related_name="cursos", blank=True,)
    professor = models.ForeignKey("contrib.Professor", on_delete=models.CASCADE, related_name="cursos",)
    data_de_criação = models.DateTimeField(auto_now_add=True,)
    ativo = models.BooleanField(default=True) 


    def __str__(self) -> str:
        return f"{self.name} | { self.professor.user.get_full_name()}"


class Gratuito(Curso):

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"Gratuito: {self.name} | {self.professor.user.get_full_name()}"
            

class Pago(Curso):
    price = models.FloatField(default=0.0)


class Video(AbstractMixin, models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    url = models.URLField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='videos')
    ordem = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.title} | {self.curso.name}"
    
    class Meta:
        ordering = ['ordem']

