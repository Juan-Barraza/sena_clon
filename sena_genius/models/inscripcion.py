from django.db import models
from sena_genius.models.curso import Curso
from sena_genius.models.usuario import Usuario


class EstadoInscripcion(models.TextChoices):
    PENDIENTE = 'Pendiente', 'Pendiente'
    ACEPTADO = 'Aceptado', 'Aceptado'
    COMPLETADO = 'Completado', 'Completado'

class Inscripcion(models.Model):
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='inscripciones',
        verbose_name='Usuario'
    )

    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name='inscritos',
        verbose_name='Curso'
    )

    fecha_inscripcion = models.DateField(
        auto_now_add=True,
        verbose_name='Fecha de inscripción'
    )

    estado = models.CharField(
        max_length=20,
        choices=EstadoInscripcion.choices,
        default='pendiente',
        verbose_name='Estado'
    )