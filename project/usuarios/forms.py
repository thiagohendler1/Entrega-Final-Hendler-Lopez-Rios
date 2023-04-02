from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label='modificar email')
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='repita contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}

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

    email = forms.EmailField()
    password1 = forms.CharField(label = 'Contraseña:', widget=forms.PasswordInput)
    password2 = forms.CharField(label = 'Repita la contraseña:', widget=forms.PasswordInput)

    # Esta parte es para hablar de los metadatos

    class Meta:
        model = User  # from django.contrib.auth.models import User
        fields = ['username', 'password1', 'password2', 'email']
        help_texts = {k:'' for k in fields}