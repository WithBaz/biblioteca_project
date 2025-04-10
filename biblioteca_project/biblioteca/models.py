from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, RegexValidator
from django.core.exceptions import ValidationError

# Usamos RegexValidator para validar que el nombre no esté vacío o solo contenga espacios
nombre_validator = RegexValidator(
    regex=r'\S',  # Al menos un carácter que no sea espacio
    message='Este campo no puede estar vacío o contener solo espacios.',
    inverse_match=False
)

class Autor(models.Model):
    nombre = models.CharField(max_length=100, validators=[nombre_validator])
    biografia = models.TextField(blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Autores"

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    # Usamos MinLengthValidator incorporado de Django
    resumen = models.TextField(validators=[MinLengthValidator(50)])
    fecha_publicacion = models.DateField()
    
    def __str__(self):
        return self.titulo
            
    class Meta:
        verbose_name_plural = "Libros"

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
