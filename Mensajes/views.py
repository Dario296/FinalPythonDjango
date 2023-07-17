from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.http import Http404, JsonResponse
from Mensajes.models import Hilo, Mensaje
from django.urls import reverse_lazy

class ListarUsuarios(LoginRequiredMixin, ListView):
    model = User
    template_name = 'perfiles/listar.html'
    
    def get(self, request, *args, **kwargs):
        listado_de_perfiles = User.objects.filter(username__icontains = "")
        return render(request, self.template_name, {'perfiles': listado_de_perfiles})
    
class DetallePerfil(DetailView):
    model = User
    template_name = 'perfiles/detalle.html'

@method_decorator(login_required, name="dispatch")
class ListaHilos(TemplateView):
    template_name = "mensajes/hilo_listas.html"

@method_decorator(login_required, name="dispatch")
class HiloDetalle(DetailView):
    model = Hilo
    template_name = "mensajes/hilo_detalle.html"
    
    def get_object(self):
        obj = super(HiloDetalle, self).get_object()
        if self.request.user not in obj.usuarios.all():
            raise Http404()
        return obj

def guardar_mensaje(request, pk):
    json_response = {'creacion':False}
    if request.user.is_authenticated:
        contenido = request.GET.get('contenido', None)
        if contenido:
            hilo = get_object_or_404(Hilo, pk=pk)  
            mensaje = Mensaje.objects.create(user=request.user, contenido=contenido)
            hilo.mensajes.add(mensaje)
            json_response['creacion'] = True
            if len(hilo.mensajes.all()) is 1:
                json_response['first'] = True
    else:
        raise Http404("User is not authenticated")

    return JsonResponse(json_response)

@login_required
def iniciar_hilo(request, username):
    user = get_object_or_404(User, username=username)
    hilo = Hilo.objects.buscar_o_crear(user, request.user)
    return redirect(reverse_lazy('detalle_mensaje', args=[hilo.pk]))