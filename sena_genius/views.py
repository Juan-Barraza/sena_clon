from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from sena_genius.models import Curso, Usuario
from sena_genius.forms import (
    CustomLoginForm,
    StudentRegistrationForm,
    CursoFiltroForm,
)


from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            documento_tipo = form.cleaned_data.get('documento_tipo')
            documento_numero = form.cleaned_data.get('documento_numero')
            password = form.cleaned_data.get('password')
            user: Usuario = authenticate(documento_numero=documento_numero, password=password)
            if user is not None and documento_tipo == user.documento_tipo:
                login(request, user)
                nombre = user.nombre or "Usuario"
                messages.success(request, f"Bienvenido {nombre}!")
                return redirect(reverse('sena_genius:home'))
            else:
                messages.error(request, "No se pudo autenticar, error al validar datos o usuario no existe.")
        else:
            messages.error(request, "Informacion de Usuario invalida.")
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})



def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'La cuenta para el estudiante {username} ha sido creada exitosamente.')
            return redirect('login')
    else:
        form = StudentRegistrationForm()
    return render(request, 'register_student.html', {'form': form})


@login_required
def home_view(request):
    cursos = Curso.objects.all()
    form = CursoFiltroForm(request.GET)

    if form.is_valid():
        categoria = form.cleaned_data.get('categoria')
        if categoria:
            cursos = cursos.filter(categoria=categoria)

    return render(request, 'home.html', {'cursos': cursos, 'form': form})

