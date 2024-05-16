from django.contrib import admin
from .models import Usuario, Curso, Inscripcion


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):

    list_display = (
        "documento_numero",
        "documento_tipo",
        "tipo_usuario",
        "nombre",
        "primer_apellido"
    )

    fields = [
        'email', 'first_name', 'last_name',
        'genero', 'estrato_socioeconomico', 'tipo_usuario',
        'nombre', 'primer_apellido', 'segundo_apellido',
        'documento_tipo', 'documento_numero', 'documento_archivo',
        'pais_expedicion', 'departamento_expedicion', 'municipio_expedicion',
        'fecha_expedicion', 'fecha_vencimiento',
        'pais_nacimiento', 'departamento_nacimiento', 'municipio_nacimiento',
        'fecha_nacimiento',
        'pais_residencia', 'departamento_residencia', 'municipio_residencia',
        'telefono_personal', 'telefono_movil',
        'contacto_nombre', 'contacto_telefono'
    ]

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    pass

@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    pass