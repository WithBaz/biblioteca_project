from django.contrib import admin
from .models import Autor, Libro, Resena

class LibroInline(admin.TabularInline):
    model = Libro
    extra = 1

class ResenaInline(admin.TabularInline):
    model = Resena
    extra = 1

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_nacimiento')
    search_fields = ('nombre',)
    inlines = [LibroInline]

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion')
    list_filter = ('autor', 'fecha_publicacion')
    search_fields = ('titulo', 'autor__nombre')
    inlines = [ResenaInline]

@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ('libro', 'calificacion', 'fecha_creacion')
    list_filter = ('calificacion', 'fecha_creacion')
    search_fields = ('libro__titulo', 'comentario')
