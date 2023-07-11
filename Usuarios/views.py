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
            return redirect('ingresar')
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

@login_required
def verPerfil(request):
    return render(request, 'registro/perfil.html')

@login_required
def editarPerfil(request): 
    info_extra_user = request.user.infoextra
    if request.method == 'POST':
        formulario = EditarPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            
            avatar = formulario.cleaned_data.get('avatar')
            fechaNacimiento = formulario.cleaned_data.get('fechaNacimiento')
            if fechaNacimiento:
                info_extra_user.fechaNacimiento = fechaNacimiento
                info_extra_user.save()
            if avatar:
                info_extra_user.avatar = avatar
                info_extra_user.save()
            
            formulario.save()
            return redirect('perfil')
    else:
        formulario = EditarPerfil(initial={'avatar': info_extra_user.avatar}, instance=request.user)
        
    return render(request, 'registro/editar.html', {'formulario': formulario})

class CambiarPassword(LoginRequiredMixin, View):
    template_name = 'registro/editarPass.html'
    form_class = CambiarPasswordForm
    success_url = reverse_lazy('perfil')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = User.objects.filter(id=request.user.id)
            if user.exists():
                user = user.first()
                user.set_password(form.cleaned_data.get('password1'))
                user.save()
                return redirect(self.success_url)
            return redirect(self.success_url)
        else:
            form = self.form_class(request.POST)
            return render(request, self.template_name, {'form': form})