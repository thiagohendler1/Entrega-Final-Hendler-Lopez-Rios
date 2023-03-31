from django.db import models
from django.contrib.auth.models import User


# Modelo para las publicaciones

class Publicacion(models.Model):
    titulo_libro = models.CharField(max_length=50)
    GENERO_CHOICES = (
        ('riqueza', 'Riqueza'),
        ('desarrollo_personal', 'Desarrollo Personal'),
        ('liderazgo', 'Liderazgo'),
        ('emprendimiento', 'Emprendimiento'),
        ('habitos', 'Habitos'),
        ('analisis_tecnico', 'Analisis Tecnico & Trading')
    )
    genero_libro = models.CharField(max_length=30, choices=GENERO_CHOICES, default='desarrollo_personal')
    autor_libro = models.CharField(max_length=30)
    editorial_libro = models.CharField(max_length=30)
    imagen_libro = models.ImageField(null=True, blank=True, upload_to='libros_publicaciones')
    descripcion = models.TextField(null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    telefono_contacto = models.IntegerField()
    email_contacto = models.EmailField()
    
    class Meta:
        # Define el ordenamiento de las publicaciones
        ordering = ['vendedor', '-fecha_publicacion']
        # Define el nombre de la tabla en el panel de administracion
        verbose_name_plural = 'Publicaciones'
    
    def __str__(self) -> str:
        return f"Usuario: {self.vendedor} - Libro: {self.titulo_libro} - {self.autor_libro}"


# Modelo para dejar un comentario en la publicacion

class Mensaje(models.Model):
    publicacion_mensaje = models.ForeignKey(Publicacion, related_name='mensajes', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    mensaje = models.TextField()
    fecha_mensaje = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-fecha_mensaje']
        
    def __str__(self) -> str:
        return f"Nombre: {self.nombre} - Publicacion: {self.publicacion_mensaje}"