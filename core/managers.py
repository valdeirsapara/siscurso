from django.db.models import Manager, Q, QuerySet
from polymorphic.models import PolymorphicModel

from . import models 

class BaseQuerySet(QuerySet):
    def ativos(self):
        return self.filter(desativado_em__isnull=True)

    def inativos(self):
        return self.filter(desativado_em__isnull=False)

class BaseManager(Manager.from_queryset(BaseQuerySet)):
    pass
