from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from Blog.models import Post
from Blog.formulario import CrearPublicacion
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

def inicio(request):
    return render ( request, 'inicio/inicio.html')

def nosotros(request):
    return render ( request, 'nosotros/nosotros.html')

class listar(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'post'
    
@login_required
def crear(request):
    if request.method == 'POST':
        formulario = CrearPublicacion(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data
            usuario = request.user
            post = Post( autor = usuario, **info )
            post.save()
            return redirect('blog')
        else:
            return render(request, 'blog/crear.html', {'formulario': formulario})
    
    formulario = CrearPublicacion()
    return render(request, 'blog/crear.html', {'formulario': formulario})

class verMas(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/verMas.html'
    
class modificar(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/modificar.html'
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']
    success_url = reverse_lazy('blog')