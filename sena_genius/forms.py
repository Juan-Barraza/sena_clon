from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from sena_genius.models import (
    Usuario,
    TipoUsuario,
    Genero,
    TipoDocumento,
    EstratoSocioeconomico,
    DepartamentoColombia,
    CategoriaCurso,
)
from sena_genius.models import TipoDocumento


class CustomLoginForm(forms.Form):
    documento_tipo = forms.ChoiceField(choices=TipoDocumento.choices, label="Tipo de Documento", widget=forms.Select(attrs={'class': 'form-control input100'}))
    documento_numero = forms.CharField(label="Número de Documento", widget=forms.TextInput(attrs={'placeholder': 'Número de documento', 'class': 'form-control input100'}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-control input100'}))

    def clean(self):
        documento_tipo = self.cleaned_data.get('documento_tipo')
        documento_numero = self.cleaned_data.get('documento_numero')
        password = self.cleaned_data.get('password')

        if documento_tipo and documento_numero and password:
            user = authenticate(documento_numero=documento_numero, password=password)
            if user is None:
                raise forms.ValidationError("Detalles de inicio de sesión incorrectos.")
        return self.cleaned_data



class StudentRegistrationForm(UserCreationForm):
    nombre = forms.CharField(max_length=150, required=True, label="Nombre")
    primer_apellido = forms.CharField(max_length=150, required=True, label="Primer apellido")
    segundo_apellido = forms.CharField(max_length=150, required=False, label="Segundo apellido")
    genero = forms.ChoiceField(choices=Genero.choices, required=False, label="Género")
    estrato_socioeconomico = forms.ChoiceField(choices=EstratoSocioeconomico.choices, required=False, label="Estrato socioeconómico")
    documento_tipo = forms.ChoiceField(choices=TipoDocumento.choices, required=True, label="Tipo de documento")
    documento_numero = forms.CharField(max_length=20, required=True, label="Número de documento")
    documento_archivo = forms.FileField(required=False, label="Archivo de documento")

    pais_expedicion = forms.CharField(required=False, label="País de expedición")
    departamento_expedicion = forms.ChoiceField(choices=DepartamentoColombia.choices, required=False, label="Departamento de expedición")
    municipio_expedicion = forms.CharField(max_length=100, required=False, label="Municipio de expedición")
    fecha_expedicion = forms.DateField(required=False, label="Fecha de expedición")
    fecha_vencimiento = forms.DateField(required=False, label="Fecha de vencimiento")

    pais_nacimiento = forms.CharField(required=False, label="País de nacimiento")
    departamento_nacimiento = forms.ChoiceField(choices=DepartamentoColombia.choices, required=False, label="Departamento de nacimiento")
    municipio_nacimiento = forms.CharField(max_length=100, required=False, label="Municipio de nacimiento")
    fecha_nacimiento = forms.DateField(required=False, label="Fecha de nacimiento")

    pais_residencia = forms.CharField(required=False, label="País de residencia")
    departamento_residencia = forms.ChoiceField(choices=DepartamentoColombia.choices, required=False, label="Departamento de residencia")
    municipio_residencia = forms.CharField(max_length=100, required=False, label="Municipio de residencia")

    telefono_personal = forms.CharField(max_length=15, required=False, label="Teléfono personal")
    telefono_movil = forms.CharField(max_length=15, required=False, label="Teléfono móvil")
    contacto_nombre = forms.CharField(max_length=100, required=False, label="Nombre de contacto")
    contacto_telefono = forms.CharField(max_length=15, required=False, label="Teléfono de contacto")

    class Meta:
        model = Usuario
        fields = ('password1', 'password2', 'email',
                  'nombre', 'primer_apellido', 'segundo_apellido', 'genero',
                  'estrato_socioeconomico', 'tipo_usuario', 'documento_tipo', 'documento_numero',
                  'documento_archivo', 'pais_expedicion', 'departamento_expedicion',
                  'municipio_expedicion', 'fecha_expedicion', 'fecha_vencimiento',
                  'pais_nacimiento', 'departamento_nacimiento', 'municipio_nacimiento',
                  'fecha_nacimiento', 'pais_residencia', 'departamento_residencia',
                  'municipio_residencia', 'telefono_personal', 'telefono_movil',
                  'contacto_nombre', 'contacto_telefono')

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.tipo_usuario = TipoUsuario.ESTUDIANTE
        if commit:
            usuario.save()
        return usuario


class CursoFiltroForm(forms.Form):
    categoria = forms.ChoiceField(
        choices=[('', 'Todas')] + list(CategoriaCurso.choices),
        required=False,
        label='Categoría'
    )

