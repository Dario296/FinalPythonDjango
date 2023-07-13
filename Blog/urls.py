from django.urls import path
from Blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.inicio, name = 'inicio'),
    path("nosotros/", views.nosotros, name = 'nosotros'),
    path("blog/", views.listar.as_view(), name = 'blog'),
    path("blog/crear/", views.crear, name = 'crear'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)