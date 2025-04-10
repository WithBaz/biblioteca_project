import os
import django
import datetime

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca_project.settings')
django.setup()

from biblioteca.models import Autor, Libro, Resena

def poblar_datos():
    # Limpiar datos existentes (opcional)
    Resena.objects.all().delete()
    Libro.objects.all().delete()
    Autor.objects.all().delete()
    
    # Crear autores
    autor1 = Autor.objects.create(
        nombre="Gabriel García Márquez",
        biografia="Escritor colombiano, premio Nobel de Literatura en 1982.",
        fecha_nacimiento=datetime.date(1927, 3, 6)
    )
    
    autor2 = Autor.objects.create(
        nombre="Isabel Allende",
        biografia="Escritora chilena, conocida por obras como 'La casa de los espíritus'.",
        fecha_nacimiento=datetime.date(1942, 8, 2)
    )
    
    autor3 = Autor.objects.create(
        nombre="Jorge Luis Borges",
        biografia="Escritor argentino, conocido por sus cuentos y ensayos.",
        fecha_nacimiento=datetime.date(1899, 8, 24)
    )
    
    # Crear libros
    libro1 = Libro.objects.create(
        titulo="Cien años de soledad",
        autor=autor1,
        resumen="Esta novela cuenta la historia de la familia Buendía a lo largo de siete generaciones en el pueblo ficticio de Macondo. Es considerada una obra maestra de la literatura latinoamericana y del realismo mágico.",
        fecha_publicacion=datetime.date(1967, 5, 30)
    )
    
    libro2 = Libro.objects.create(
        titulo="El amor en los tiempos del cólera",
        autor=autor1,
        resumen="Esta novela narra la historia de amor entre Florentino Ariza y Fermina Daza, que esperan más de medio siglo para estar juntos. Es una exploración del amor en todas sus formas.",
        fecha_publicacion=datetime.date(1985, 1, 1)
    )
    
    libro3 = Libro.objects.create(
        titulo="La casa de los espíritus",
        autor=autor2,
        resumen="Esta novela narra la vida de la familia Trueba a lo largo de cuatro generaciones, y la historia post-colonial de Chile. Es la primera novela de Isabel Allende y su obra más conocida.",
        fecha_publicacion=datetime.date(1982, 1, 1)
    )
    
    libro4 = Libro.objects.create(
        titulo="El Aleph",
        autor=autor3,
        resumen="Esta colección de cuentos explora temas como la infinitud, el tiempo y la realidad. El cuento que da título al libro describe un punto en el espacio que contiene todos los demás puntos.",
        fecha_publicacion=datetime.date(1949, 1, 1)
    )
    
    # Crear reseñas
    Resena.objects.create(
        libro=libro1,
        calificacion=5,
        comentario="Una obra maestra absoluta. La forma en que García Márquez entrelaza realidad y fantasía es incomparable."
    )
    
    Resena.objects.create(
        libro=libro1,
        calificacion=4,
        comentario="Fascinante pero complejo. A veces es difícil seguir todas las generaciones de la familia Buendía."
    )
    
    Resena.objects.create(
        libro=libro2,
        calificacion=5,
        comentario="Una hermosa historia de amor y paciencia. La prosa de García Márquez es poética y cautivadora."
    )
    
    Resena.objects.create(
        libro=libro3,
        calificacion=4,
        comentario="Una poderosa saga familiar con elementos de realismo mágico. Allende crea personajes femeninos memorables."
    )
    
    Resena.objects.create(
        libro=libro4,
        calificacion=5,
        comentario="Borges demuestra su genio en cada página. Sus ideas sobre el infinito y la realidad son fascinantes."
    )
    
    print("Datos poblados exitosamente!")

if __name__ == "__main__":
    print("Iniciando script de población de datos...")
    poblar_datos()
    print("Población de datos completada!")
