from django.contrib import admin
from django.db import transaction
from django.utils import timezone
from django.utils.translation import gettext_lazy as _ 

# Modulos locais
from . import models


def desativar(modeladmin, request, queryset):
    with transaction.atomic():
        queryset.update(
            desativado_por=request.user,
            desativado_em=timezone.now()
        )
desativar.short_description = "Desativa selecionados"

def reativar(modeladmin, request, queryset):

    with transaction.atomic():
        queryset.update(
            modificado_por=request.user,
            modificado_em=timezone.now(),
            desativado_por=None,
            desativado_em=None
        )

reativar.short_description = "Reativa selecionados"


class AtivoListFilter(admin.SimpleListFilter):
    title = _('Ativo')
    parameter_name = 'ativo'

    def lookups(self, request, model_admin):
        return (
            (True, _('Ativos')),
            (False, _('Inativos')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'True':
            return queryset.filter(desativado_em__isnull=True)
        elif self.value() == 'False':
            return queryset.filter(desativado_em__isnull=False)
        return queryset
    
class AbstractAdmin(admin.ModelAdmin):
    actions = [desativar, reativar]
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)

        if not self.readonly_fields:
            self.readonly_fields = tuple()

        self.readonly_fields = self.readonly_fields + (
            'cadastrado_por',
            'cadastrado_em',
            'modificado_por',
            'modificado_em',
            'desativado_por',
            'desativado_em'
        )

        if not self.list_filter:
            self.list_filter = tuple()

        self.list_filter = (AtivoListFilter,) + self.list_filter