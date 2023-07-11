from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    titulo = models.CharField(max_length = 30)
    subtitulo = models.CharField(max_length = 50)
    cuerpo = models.TextField(default = '')
    imagen = models.ImageField()
    fecha = models.DateField(auto_now_add = True)
    autor = models.OneToOneField(User, on_delete = models.CASCADE)