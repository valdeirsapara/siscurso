from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html_join

from .models import Professor, Aluno
from .forms import CustomUserCreationForm

# Register your models here.
class ProfessorInline(admin.StackedInline):
    model = Professor
    can_delete = False
    verbose_name_plural = 'Professor'
    fk_name = 'user'
    readonly_fields = ['cursos_ministrados']

    def cursos_ministrados(self, obj):
        if not obj or not obj.pk:
            return "Salve o usuário primeiro"
        cursos = obj.cursos.all()
        if not cursos.exists():
            return "Nenhum curso ministrado"
        return format_html_join('\n', "<li>{}</li>", ((curso.name,) for curso in cursos))
    cursos_ministrados.short_description = "Cursos Ministrados"




class AlunoInline(admin.StackedInline):
    model = Aluno
    can_delete = False
    verbose_name_plural = 'Aluno'
    fk_name = 'user'
    readonly_fields = ['cursos_inscritos']

    def cursos_inscritos(self, obj):
        if hasattr(obj,'aluno'):
            cursos = obj.aluno.cursos.all()
            if cursos.exists():
                return format_html_join(
                    '\n', '<li>{}</li>',((curso.name,) for curso in cursos)
                )
            return "Nenhum curso inscrito"

        return "User não é Aluno"


class CustomUserAdmin(UserAdmin):
    inlines = [ProfessorInline, AlunoInline]

    form = CustomUserCreationForm

    add_form = CustomUserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2',),
        }),
    )
    
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return []
        return super().get_inline_instances(request, obj)
    
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)