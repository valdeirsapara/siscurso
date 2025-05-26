from django.db import models
from django_currentuser.db.models import CurrentUserField
from django.utils import timezone

from . import managers

class AbstractMixin(models.Model):
    cadastrado_por = CurrentUserField(
        null=True,
        on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_cadastrado_por'
    )
    cadastrado_em = models.DateTimeField(
        auto_now_add=True,
        null=True
    )
    modificado_por = CurrentUserField(
        null=True,
        on_update=True,
        on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_modificado_por'
    )
    modificado_em = models.DateTimeField(
        auto_now=True,
        null=True
    )

    desativado_por = models.ForeignKey(
        to='auth.User',
        null=True,
        on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_desativado_por',
        blank=True
    )

    desativado_em = models.DateTimeField(
        null=True,
        blank=True
    )
    objects = managers.BaseManager()

    class Meta:
        abstract = True

    def _ativo(self):
        return self.desativado_em is None
    
    _ativo.boolean = True
    ativo = property(_ativo)

    def desativar(self,usuario, data_hora=None):
        if data_hora is None:
            data_hora = timezone.now()

        self.modificado_por = usuario
        self.modificado_em = data_hora

        self.desativado_por = usuario
        self.desativado_em = data_hora
        self.save()


    def reativar(self, usuario, data_hora=None):
        if data_hora is None:
            data_hora = timezone.now()

        self.modificado_por = usuario
        self.modificado_em = data_hora

        self.desativado_por = None
        self.desativado_em = None
        self.save()
