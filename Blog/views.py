from django.shortcuts import render
from django.views.generic.list import ListView
from Blog.models import Post
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    return render ( request, 'inicio/inicio.html')

def nosotros(request):
    return render ( request, 'nosotros/nosotros.html')

class listar(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'post'
    
class crear(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/crear.html'
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']
    success_url = reverse_lazy('Blog:blog')