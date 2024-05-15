from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField

from sena_genius.managers import UsuarioManager


class Genero(models.TextChoices):
    MASCULINO = 'Masculino', 'Masculino'
    FEMENINO = 'Femenino', 'Femenino'
    NO_BINARIO = 'No binario', 'No binario'

class TipoUsuario(models.TextChoices):
    ESTUDIANTE = 'Estudiante', 'Estudiante'
    PROFESOR = 'Profesor', 'Profesor'
    ADMINISTRADOR = 'Administrador', 'Administrador'

class TipoDocumento(models.TextChoices):
    CEDULA_CIUDADANIA = 'CC', 'Cédula de Ciudadanía'
    TARJETA_IDENTIDAD = 'TI', 'Tarjeta de Identidad'
    CEDULA_EXTRANJERIA = 'CE', 'Cédula de Extranjería'
    PERMISO_PERMANENCIA = 'PP', 'PEP'
    PROTECCION_TEMPORAL = 'PT', 'Permiso por Protección Temporal'

class EstratoSocioeconomico(models.TextChoices):
    UNO = '1', 'Uno'
    DOS = '2', 'Dos'
    TRES = '3', 'Tres'
    CUATRO = '4', 'Cuatro'
    CINCO = '5', 'Cinco'
    SEIS = '6', 'Seis'

class DepartamentoColombia(models.TextChoices):
    AMAZONAS = 'Amazonas', 'Amazonas'
    ANTIOQUIA = 'Antioquia', 'Antioquia'
    ARAUCA = 'Arauca', 'Arauca'
    ATLANTICO = 'Atlántico', 'Atlántico'
    BOGOTA = 'Bogotá, D.C.', 'Bogotá, D.C.'
    BOLIVAR = 'Bolívar', 'Bolívar'
    BOYACA = 'Boyacá', 'Boyacá'
    CALDAS = 'Caldas', 'Caldas'
    CAQUETA = 'Caquetá', 'Caquetá'
    CASANARE = 'Casanare', 'Casanare'
    CAUCA = 'Cauca', 'Cauca'
    CESAR = 'Cesar', 'Cesar'
    CHOCO = 'Chocó', 'Chocó'
    CORDOBA = 'Córdoba', 'Córdoba'
    CUNDINAMARCA = 'Cundinamarca', 'Cundinamarca'
    GUAINIA = 'Guainía', 'Guainía'
    GUAVIARE = 'Guaviare', 'Guaviare'
    HUILA = 'Huila', 'Huila'
    LA_GUAJIRA = 'La Guajira', 'La Guajira'
    MAGDALENA = 'Magdalena', 'Magdalena'
    META = 'Meta', 'Meta'
    NARINO = 'Nariño', 'Nariño'
    NORTE_DE_SANTANDER = 'Norte de Santander', 'Norte de Santander'
    PUTUMAYO = 'Putumayo', 'Putumayo'
    QUINDIO = 'Quindío', 'Quindío'
    RISARALDA = 'Risaralda', 'Risaralda'
    SAN_ANDRES = 'San Andrés y Providencia', 'San Andrés y Providencia'
    SANTANDER = 'Santander', 'Santander'
    SUCRE = 'Sucre', 'Sucre'
    TOLIMA = 'Tolima', 'Tolima'
    VALLE_DEL_CAUCA = 'Valle del Cauca', 'Valle del Cauca'
    VAUPES = 'Vaupés', 'Vaupés'
    VICHADA = 'Vichada', 'Vichada'


class Usuario(AbstractUser):
    genero = models.CharField(
        max_length=20,
        choices=Genero.choices,
        blank=True,
        null=True,
        verbose_name='Género'
    )
    estrato_socioeconomico = models.CharField(
        max_length=1,
        choices=EstratoSocioeconomico.choices,
        blank=True,
        null=True,
        verbose_name='Estrato socioeconómico'
    )
    tipo_usuario = models.CharField(
        max_length=20,
        choices=TipoUsuario.choices,
        default=TipoUsuario.ESTUDIANTE,
        blank=True,
        null=True,
        verbose_name='Tipo de usuario'
    )

    #? Nombres
    nombre = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name='Nombre'
    )
    primer_apellido = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name='Primer apellido'
    )
    segundo_apellido = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name='Segundo apellido'
    )

    #? Documento
    documento_tipo = models.CharField(
        max_length=50,
        choices=TipoDocumento.choices,
        blank=True,
        null=True,
        verbose_name='Tipo de documento'
    )
    documento_numero = models.CharField(
        max_length=50,
        unique=True,
        blank=True,
        null=True,
        verbose_name='Número de documento'
    )
    documento_archivo = models.FileField(
        upload_to='documentos/',
        blank=True,
        null=True,
        verbose_name='Archivo de documento'
    )

    #? Expedición de documento
    pais_expedicion = CountryField(
        blank=True,
        null=True,
        verbose_name='País de expedición'
    )
    departamento_expedicion = models.CharField(
        max_length=50,
        choices=DepartamentoColombia.choices,
        blank=True,
        null=True,
        verbose_name='Departamento de expedición'
    )
    municipio_expedicion = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Municipio de expedición'
    )
    fecha_expedicion = models.DateField(
        blank=True,
        null=True,
        verbose_name='Fecha de expedición'
    )
    fecha_vencimiento = models.DateField(
        blank=True,
        null=True,
        verbose_name='Fecha de vencimiento'
    )

    #? Nacimiento
    pais_nacimiento = CountryField(
        blank=True,
        null=True,
        verbose_name='País de nacimiento'
    )
    departamento_nacimiento = models.CharField(
        max_length=50,
        choices=DepartamentoColombia.choices,
        blank=True,
        null=True,
        verbose_name='Departamento de nacimiento'
    )
    municipio_nacimiento = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Municipio de nacimiento'
    )
    fecha_nacimiento = models.DateField(
        blank=True,
        null=True,
        verbose_name='Fecha de nacimiento'
    )

    #? Residencia
    pais_residencia = CountryField(
        blank=True,
        null=True,
        verbose_name='País de residencia'
    )
    departamento_residencia = models.CharField(
        max_length=50,
        choices=DepartamentoColombia.choices,
        blank=True,
        null=True,
        verbose_name='Departamento de residencia'
    )
    municipio_residencia = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Municipio de residencia'
    )

    #? Datos de contacto
    telefono_personal = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name='Teléfono personal'
    )
    telefono_movil = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name='Teléfono móvil'
    )

    #? Contacto asociado
    contacto_nombre = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Nombre de contacto'
    )
    contacto_telefono = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name='Teléfono de contacto'
    )

    USERNAME_FIELD = "documento_numero"
    objects = UsuarioManager()

    def __str__(self):
        return f"{self.documento_numero}"