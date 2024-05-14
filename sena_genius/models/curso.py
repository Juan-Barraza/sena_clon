from django.db import models


class CategoriaCurso(models.TextChoices):
    TECNICO = 'Técnico', 'Técnico'
    TECNOLOGICO = 'Tecnológico', 'Tecnológico'
    ESPECIALIZACION = 'Especialización', 'Especialización'
    COMPLEMENTARIO = 'Complementario', 'Complementario'

class Curso(models.Model):
    nombre = models.CharField(
        max_length=200,
        verbose_name='Nombre'
    )

    descripcion = models.TextField(
        verbose_name='Descripción'
    )

    requisitos = models.TextField(
        verbose_name='Requisitos'
    )

    fecha_inicio = models.DateField(
        verbose_name='Fecha de inicio'
    )

    categoria = models.CharField(
        max_length=50,
        choices=CategoriaCurso.choices,
        verbose_name='Categoría'
    )