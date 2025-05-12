from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Aluno, Professor




class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email")

    def save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()
            Professor.objects.create(user=user)
            Aluno.objects.create(user=user)

        return user
