from django.contrib import admin
from .models import Curso, Video
from core.admin import AbstractAdmin

# Register your models here.

    
class VideoAdmin(AbstractAdmin):
    pass

class VideoInline(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'url', 'ordem')
    readonly_fields = ('created_at', 'updated_at')

class CursoAdmin(AbstractAdmin):
    inlines = [VideoInline]
    
admin.site.register(Curso, CursoAdmin)
admin.site.register(Video, VideoAdmin)