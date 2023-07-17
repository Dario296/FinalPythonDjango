from django.urls import path
from Mensajes import views

urlpatterns = [
    path("lista_usuarios", views.ListarUsuarios.as_view(), name = 'lista_usuarios'),
    path('lista_usuarios/<int:pk>/', views.DetallePerfil.as_view(), name='detalle'),
    path('mensajes', views.ListaHilos.as_view(), name="mensajes"),
    path('hilo/<int:pk>/', views.HiloDetalle.as_view(), name="detalle_mensaje"),
    path('hilo/<int:pk>/enviar/', views.guardar_mensaje, name="enviar"),
    path('hilo/iniciar_hilo/<username>/', views.iniciar_hilo, name="iniciar_hilo"),
]