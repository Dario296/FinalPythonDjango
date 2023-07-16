from django import forms
from ckeditor.fields import RichTextFormField

class CrearPublicacion(forms.Form):
    titulo = forms.CharField()
    subtitulo = forms.CharField(required=False)
    cuerpo = RichTextFormField()
    imagen = forms.ImageField(required=False)
    
class MostrarPost(forms.Form):
    nombre = forms.CharField(max_length=20, required=False, label="", widget= forms.TextInput(
        attrs={
        'placeholder': 'Buscar Titulo',
        'class': "form-control me-2",
    }))