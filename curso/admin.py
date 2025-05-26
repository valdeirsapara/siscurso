from django.contrib import admin
from .models import Curso
from core.admin import AbstractAdmin

# Register your models here.

class CursoAdmin(AbstractAdmin):
    pass
    

admin.site.register(Curso, CursoAdmin)