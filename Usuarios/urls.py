from django.urls import path
from Usuarios import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("registrarse/", views.registrarse, name = 'registrarse'),
    path("ingresar/", views.ingresar, name = 'ingresar'),
    path("salir/", LogoutView.as_view(template_name='ingresar/salir.html'), name = 'salir'),
    path("perfil/", views.verPerfil , name = 'perfil'),
    path("perfil/editar/", views.editar_perfil , name = 'editar_perfil'),
    path("perfil/editar_password/", views.CambiarPassword.as_view(), name = 'editar_password'),
]