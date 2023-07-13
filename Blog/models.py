from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Post(models.Model):
    titulo = models.CharField(max_length = 30)
    subtitulo = models.CharField(max_length = 50, null=True, blank=True)
    cuerpo = RichTextField(default = '')
    imagen = models.ImageField(upload_to='publicaciones', null=True, blank=True)
    fecha = models.DateField(auto_now_add = True)
    autor = models.ForeignKey(User, on_delete = models.CASCADE)