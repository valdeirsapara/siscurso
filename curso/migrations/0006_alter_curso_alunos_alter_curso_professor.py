# Generated by Django 5.2 on 2025-04-14 23:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrib', '0001_initial'),
        ('curso', '0005_alter_curso_alunos_alter_curso_data_de_criação_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='alunos',
            field=models.ManyToManyField(related_name='cursos', to='contrib.aluno'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cursos', to='contrib.professor'),
        ),
    ]
