
from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso
from .forms import CursoForm

def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/lista.html', {'cursos': cursos})

def detalhe_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    return render(request, 'cursos/detalhe.html', {'curso': curso})

def cadastrar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm()
    return render(request, 'cursos/cadastro.html', {'form': form})

def editar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)

    if request.user != curso.professor.usuario and not request.user.is_superuser:
        return redirect('detalhe_curso', curso_id=curso.id)

    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('detalhe_curso', curso_id=curso.id)
    else:
        form = CursoForm(instance=curso)

    return render(request, 'curso/editar_curso.html', {'form': form, 'curso': curso})