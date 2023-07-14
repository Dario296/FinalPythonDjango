from django.urls import path
from Blog import views

urlpatterns = [
    path("", views.inicio, name = 'inicio'),
    path("nosotros/", views.nosotros, name = 'nosotros'),
    path("blog/", views.Listar.as_view(), name = 'blog'),
    path("blog/crear/", views.crear, name = 'crear'),
    path("blog/ver_mas/<int:pk>/", views.VerMas.as_view(), name = 'ver_mas'),
    path("blog/modificar/<int:pk>/", views.Modificar.as_view(), name = 'modificar'),
    path("blog/eliminar/<int:pk>/", views.Eliminar.as_view(), name = 'eliminar'),
]