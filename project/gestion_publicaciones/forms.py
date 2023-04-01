from django import forms
from gestion_publicaciones.models import Publicacion, Mensaje


# Formulario para crear una publicacion

class NuevaPublicacionForm(forms.ModelForm):
    
    class Meta:
        model = Publicacion
        fields = ('titulo_libro', 'genero_libro', 'autor_libro', 'editorial_libro', 'imagen_libro', 'descripcion', 'precio', 'vendedor', 'telefono_contacto', 'email_contacto')
        
        # Widgets para personalizar el formulario con CSS
        widgets = {
            'titulo_libro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo del libro'}),
            'genero_libro': forms.Select(attrs={'class': 'form-control'}),
            'autor_libro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Autor del libro'}),
            'editorial_libro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Editorial del libro'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Añade una descripcion', 'required': False}),
            'precio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor del producto', 'maxlenght': '12', 'type': 'number'}),
            'vendedor': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'vendedor_id', 'type': 'hidden'}),
            'telefono_contacto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefono de contacto', 'type': 'number'}),
            'email_contacto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email de contacto'})
        }