from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html_join

from .models import Professor, Aluno, Ordem

# Register your models here.
class ProfessorInline(admin.StackedInline):
    model = Professor
    can_delete = False
    verbose_name_plural = 'Professor'
    fk_name = 'user'


class OrdemAdmin(admin.ModelAdmin):
    model = Ordem
    list_display = ('id', 'aluno', 'status',)
    
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    list_filter = ('status',)
    search_fields = ('aluno__user__username', 'curso__title')
    readonly_fields = ('data_pagamento','aluno', 'curso', 'status', 'valor',)

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
admin.site.register(Ordem, OrdemAdmin)