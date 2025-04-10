from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
import datetime

def validate_not_empty_or_whitespace(value):
    if value.strip() == '':
        raise ValidationError('Este campo no puede estar vacío o contener solo espacios.')

def validate_min_length(min_length):
    def validator(value):
        if len(value) < min_length:
            raise ValidationError(f'Este campo debe tener al menos {min_length} caracteres.')
    return validator

class Autor(models.Model):
    nombre = models.CharField(max_length=100, validators=[validate_not_empty_or_whitespace])
    biografia = models.TextField(blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Autores"

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    resumen = models.TextField(validators=[validate_min_length(50)])
    fecha_publicacion = models.DateField()
    
    def __str__(self):
        return self.titulo

class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='resenas')
    calificacion = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comentario = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Reseña de {self.libro.titulo} - {self.calificacion}/5"
    
    class Meta:
        verbose_name = "Reseña"
        verbose_name_plural = "Reseñas"
