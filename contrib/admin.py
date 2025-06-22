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



class AlunoInline(admin.StackedInline):
    model = Aluno
    can_delete = False
    verbose_name_plural = 'Aluno'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = [ProfessorInline, AlunoInline]
    
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return []
        return super().get_inline_instances(request, obj)
    
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)