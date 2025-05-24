
from django.shortcuts import render, get_object_or_404
from .models import Curso

def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/lista.html', {'cursos': cursos})

def detalhe_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    return render(request, 'cursos/detalhe.html', {'curso': curso})
