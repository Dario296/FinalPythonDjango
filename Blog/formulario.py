from django import forms
from ckeditor.fields import RichTextFormField

class CrearPublicacion(forms.Form):
    titulo = forms.CharField()
    subtitulo = forms.CharField(required=False)
    cuerpo = RichTextFormField()
    imagen = forms.ImageField(required=False)