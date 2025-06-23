
from django import forms
from .models import Pago

class CursoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['name', 'description', 'duracao', 'price', 'professor', 'ativo']
