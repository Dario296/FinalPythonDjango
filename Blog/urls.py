from django.urls import path
from Blog import views

urlpatterns = [
    path("", views.inicio, name = 'inicio'),
    path("nosotros/", views.nosotros, name = 'nosotros'),
    path("blog/", views.listar.as_view(), name = 'blog'),
    path("blog/crear/", views.crear, name = 'crear'),
    path("blog/verMas/<int:pk>/", views.verMas.as_view(), name = 'verMas'),
    path("blog/modificar/<int:pk>/", views.modificar.as_view(), name = 'modificar'),
]