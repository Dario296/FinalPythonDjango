from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from Blog.models import Post
from Blog.formulario import CrearPublicacion

def inicio(request):
    return render ( request, 'inicio/inicio.html')

def nosotros(request):
    return render ( request, 'nosotros/nosotros.html')

class listar(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'post'
    
def crear(request):
    if request.method == 'POST':
        formulario = CrearPublicacion(request.POST)
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