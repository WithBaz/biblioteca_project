from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import Autor, Libro, Resena
from .serializers import AutorSerializer, LibroSerializer, ResenaSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    
    def get_queryset(self):
        queryset = Autor.objects.all()
        nombre = self.request.query_params.get('nombre', None)
        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)
        return queryset

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    # Agregamos filtros por autor y fecha de publicación usando django-filter
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['autor', 'fecha_publicacion']
    ordering_fields = ['titulo', 'fecha_publicacion']
    
    # Creamos una ruta personalizada para calcular el promedio de calificaciones de un libro
    @action(detail=True, methods=['get'])
    def resenas_promedio(self, request, pk=None):
        libro = self.get_object()
        resenas = libro.resenas.all()
        
        if not resenas:
            return Response({"promedio": "No hay reseñas para este libro"})
        
        promedio = sum(resena.calificacion for resena in resenas) / resenas.count()
        return Response({"promedio": round(promedio, 2)})

class ResenaViewSet(viewsets.ModelViewSet):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['libro', 'calificacion']
    ordering_fields = ['fecha_creacion', 'calificacion']
    
    def perform_create(self, serializer):
        serializer.save()
