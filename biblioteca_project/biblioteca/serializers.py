from rest_framework import serializers
from .models import Autor, Libro, Resena

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nombre', 'biografia', 'fecha_nacimiento']

class ResenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resena
        fields = ['id', 'libro', 'calificacion', 'comentario', 'fecha_creacion']

class LibroSerializer(serializers.ModelSerializer):
    autor_nombre = serializers.ReadOnlyField(source='autor.nombre')
    
    resenas_recientes = serializers.SerializerMethodField()
    
    class Meta:
        model = Libro
        fields = ['id', 'titulo', 'autor', 'autor_nombre', 'resumen', 'fecha_publicacion', 'resenas_recientes']
    
    def get_resenas_recientes(self, obj):
        resenas = obj.resenas.order_by('-fecha_creacion')[:5]
        return ResenaSerializer(resenas, many=True).data
