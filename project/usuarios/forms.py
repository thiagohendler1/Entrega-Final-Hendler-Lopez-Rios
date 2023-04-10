from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from usuarios.models import Avatar


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


# class UserEditForm(UserCreationForm):
#     email = forms.EmailField(label='modificar email')
#     password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='repita contraseña', widget=forms.PasswordInput)
    
#     class Meta:
#         model = User
#         fields = ['email', 'password1', 'password2']
#         help_texts = {k:'' for k in fields}


class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label='Nuevo email', widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Nueva direccion email', 'required': False}))
    first_name = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre', 'required': False}))
    last_name = forms.CharField(label='Apellidos', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos', 'required': False}))
    username = forms.CharField(label='Nuevo Nombre de Usuario', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nuevo Nombre de Usuario', 'required': False}))
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username']


# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
#     password1 = forms.CharField(label='Contraseña', widget= forms.PasswordInput)
#     password2 = forms.CharField(label='Repite la contraseña', widget= forms.PasswordInput)
    
#     class Meta: 
#         model = User
#         fields = ['username', 'password1', 'password2', 'email']
#         help_texts= {k:"" for k in fields}
        
        
class UserRegisterForm(UserCreationForm):
    # Aca es donde se personaliza el formulario de registro
    # Las variables se deben llamar obligatoriamente como se ven debajo

    first_name = forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre'}))
    last_name = forms.CharField(max_length=20, label='Apellidos', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Apellidos'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electronico'}))
    password1 = password1 = forms.CharField(label = 'Contraseña:', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
    password2 = password2 = forms.CharField(label = 'Repetir contraseña:', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repita la Contraseña'}))
    
    # Esta parte es para hablar de los metadatos
    class Meta:
        model = User  # from django.contrib.auth.models import User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de Usuario'})
        }


class CustomAuthenticationForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['username'].widget.attrs['class'] = 'form-control form-control-login'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password'].widget.attrs['class'] = 'form-control form-control-login'


class PasswordEditForm(PasswordChangeForm):
    old_password = forms.CharField(label='Contraseña actual', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña actual'}))
    new_password1 = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Nueva contraseña'}))
    new_password2 = forms.CharField(label='Repetir nueva contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repetir nueva contraseña'}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        
        
class AvatarForm(forms.ModelForm):
    
    class Meta:
        model = Avatar
        fields = ['imagen']
        widgets = {
            'imagen': forms.FileInput(attrs={'class': 'form-control form-control-avatar'})
        }