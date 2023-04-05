from django import forms
from gestion_publicaciones.models import Publicacion, Mensaje


class NuevaPublicacionForm(forms.ModelForm):
    # Formulario para crear una publicacion
    
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
            'precio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor del producto', 'maxlenght': '12', 'type': 'number', 'step': '.01'}),
            'vendedor': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'vendedor_id', 'type': 'hidden', 'required': False}),
            'telefono_contacto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefono de contacto', 'type': 'number'}),
            'email_contacto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email de contacto'}),
            'imagen_libro': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Editorial del libro'})
        }
        

class EditarPublicacionForm(forms.ModelForm):
    # Formulario para editar una publicacion
    
    class Meta:
        model = Publicacion
        fields = ('titulo_libro', 'genero_libro', 'autor_libro', 'editorial_libro', 'imagen_libro', 'descripcion', 'precio', 'telefono_contacto', 'email_contacto')
        
        # Widgets para personalizar el formulario con CSS
        widgets = {
            'titulo_libro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo del libro'}),
            'genero_libro': forms.Select(attrs={'class': 'form-control'}),
            'autor_libro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Autor del libro'}),
            'editorial_libro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Editorial del libro'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Añade una descripcion', 'required': False}),
            'precio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor del producto', 'maxlenght': '12', 'type': 'number'}),
            'telefono_contacto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefono de contacto', 'type': 'number'}),
            'email_contacto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email de contacto'})
        }


class MensajeForm(forms.ModelForm):
    # Formulario para crear un mensaje de publicacion
    
    class Meta:
        model = Mensaje
        fields = ('publicacion_mensaje', 'mensaje')
        
        # Widgets para personalizar el formulario con CSS
        widgets = {
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mensaje'}),
            'publicacion_mensaje': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'publicacion_mensaje_id', 'type': 'hidden'})
        }