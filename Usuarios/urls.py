from django.urls import path
from Usuarios import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("registrarse/", views.registrarse, name = 'registrarse'),
    path("ingresar/", views.ingresar, name = 'ingresar'),
    path("salir/", LogoutView.as_view(template_name='ingresar/salir.html'), name = 'salir'),
    path("perfil/", views.verPerfil , name = 'perfil'),
    path("perfil/editar/", views.editarPerfil , name = 'editarPerfil'),
    path("perfil/editarPassword/", views.CambiarPassword.as_view(), name = 'editarPassword'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)