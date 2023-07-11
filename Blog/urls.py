from django.urls import path
from Blog import views

urlpatterns = [
    path("", views.inicio, name = 'inicio'),
    path("nosotros/", views.nosotros, name = 'nosotros'),
    path("blog/", views.listar.as_view(), name = 'blog'),
    path("blog/crear/", views.crear.as_view(), name = 'crear'),
]