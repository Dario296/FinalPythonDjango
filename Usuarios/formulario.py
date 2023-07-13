from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class CrearUsuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Repetir Contraseña', widget = forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {k:"" for k in fields}
        
class EditarPerfil(UserChangeForm):
    password = None
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre', max_length=20)    
    last_name = forms.CharField(label='Apellido', max_length=20)  
    avatar = forms.ImageField(label='Imagen/avatar', required=False)
    fechaNacimiento = forms.DateField(label= 'Fecha de Nacimiento', required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'avatar', 'fechaNacimiento']
        
class CambiarPasswordForm(forms.Form):
    password1 = forms.CharField(label = 'Contraseña',widget = forms.PasswordInput(
        attrs = {
            'placeholder': 'Ingrese su nueva contraseña...',
            'required':'required',
        }
    ))

    password2 = forms.CharField(label = 'Contraseña de Confirmación', widget = forms.PasswordInput(
        attrs={
            'placeholder': 'Ingrese nuevamente la nueva contraseña...',
            'required': 'required',
        }
    ))

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden!')
        return password2