from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from Blog.models import Post
from Blog.formulario import CrearPublicacion, MostrarPost
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

def inicio(request):
    return render ( request, 'inicio/inicio.html')

def nosotros(request):
    return render ( request, 'nosotros/nosotros.html')

class Listar(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'post'
    form_class = MostrarPost
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(request.GET)
        if form.is_valid():
            nombre_a_buscar = form.cleaned_data['nombre']
            listado_de_post = Post.objects.filter(titulo__icontains = nombre_a_buscar)
            if Post.objects.count() == 0:
                return render(request, self.template_name, {'form': self.form_class, 'post': None})
            elif listado_de_post:
                return render(request, self.template_name, {'form': self.form_class, 'post': listado_de_post})
            else:
                return render(request, self.template_name, {'form': self.form_class, 'resultado': "No se encontraron resultados para la búsqueda en el blog..."})
        return render(request, self.template_name, {'form': self.form_class, 'post': listado_de_post})
    
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

class VerMas(DetailView):
    model = Post
    template_name = 'blog/ver_mas.html'
    
class Modificar(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/modificar.html'
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']
    success_url = reverse_lazy('blog')
    
class Eliminar(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/eliminar.html"
    success_url = reverse_lazy('blog')