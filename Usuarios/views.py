from django.shortcuts import render, redirect
from Usuarios.formulario import CrearUsuario, EditarPerfil, CambiarPasswordForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from Usuarios.models import InfoExtra
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.contrib.auth.models import User

def registrarse(request):
    if request.method == 'POST':
        formulario = CrearUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
        else:
            return render(request, 'registro/registro.html', {'formulario': formulario})
    
    formulario = CrearUsuario()
    return render(request, 'registro/registro.html', {'formulario': formulario})

def ingresar(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            contrasenia = formulario.cleaned_data['password']
            
            user = authenticate(username=usuario, password=contrasenia)
            
            login(request, user)
            InfoExtra.objects.get_or_create(user=user)
            
            return redirect('inicio')
        else:
            return render(request, 'ingresar/ingresar.html', {'formulario': formulario})
        
    formulario = AuthenticationForm()
    return render(request, 'ingresar/ingresar.html', {'formulario': formulario})