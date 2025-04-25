import os
import django
import datetime
import random

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
    autores = [
        Autor.objects.create(
            nombre="Gabriel García Márquez",
            biografia="Escritor colombiano, premio Nobel de Literatura en 1982.",
            fecha_nacimiento=datetime.date(1927, 3, 6)
        ),
        Autor.objects.create(
            nombre="Isabel Allende",
            biografia="Escritora chilena, conocida por obras como 'La casa de los espíritus'.",
            fecha_nacimiento=datetime.date(1942, 8, 2)
        ),
        Autor.objects.create(
            nombre="Jorge Luis Borges",
            biografia="Escritor argentino, conocido por sus cuentos y ensayos.",
            fecha_nacimiento=datetime.date(1899, 8, 24)
        ),
        Autor.objects.create(
            nombre="Julio Cortázar",
            biografia="Escritor argentino, conocido por su obra 'Rayuela'.",
            fecha_nacimiento=datetime.date(1914, 8, 26)
        ),
        Autor.objects.create(
            nombre="Mario Vargas Llosa",
            biografia="Escritor peruano, premio Nobel de Literatura en 2010.",
            fecha_nacimiento=datetime.date(1936, 3, 28)
        )
    ]
    
    # Crear libros
    libros = [
        Libro.objects.create(
            titulo="Cien años de soledad",
            autor=autores[0],
            resumen="Esta novela cuenta la historia de la familia Buendía a lo largo de siete generaciones en el pueblo ficticio de Macondo.",
            fecha_publicacion=datetime.date(1967, 5, 30)
        ),
        Libro.objects.create(
            titulo="El amor en los tiempos del cólera",
            autor=autores[0],
            resumen="Esta novela narra la historia de amor entre Florentino Ariza y Fermina Daza.",
            fecha_publicacion=datetime.date(1985, 1, 1)
        ),
        Libro.objects.create(
            titulo="La casa de los espíritus",
            autor=autores[1],
            resumen="Esta novela narra la vida de la familia Trueba a lo largo de cuatro generaciones.",
            fecha_publicacion=datetime.date(1982, 1, 1)
        ),
        Libro.objects.create(
            titulo="El Aleph",
            autor=autores[2],
            resumen="Esta colección de cuentos explora temas como la infinitud, el tiempo y la realidad.",
            fecha_publicacion=datetime.date(1949, 1, 1)
        ),
        Libro.objects.create(
            titulo="Rayuela",
            autor=autores[3],
            resumen="Una novela que puede leerse de múltiples maneras, siguiendo el orden propuesto por el autor o en el orden tradicional.",
            fecha_publicacion=datetime.date(1963, 6, 28)
        ),
        Libro.objects.create(
            titulo="La ciudad y los perros",
            autor=autores[4],
            resumen="La novela narra la vida de un grupo de cadetes en el Colegio Militar Leoncio Prado de Lima.",
            fecha_publicacion=datetime.date(1963, 1, 1)
        )
    ]
    
    # Crear reseñas con calificaciones decimales
    comentarios = [
        "Una obra maestra absoluta.",
        "Fascinante pero complejo.",
        "Una hermosa historia de amor y paciencia.",
        "Una poderosa saga familiar con elementos de realismo mágico.",
        "El autor demuestra su genio en cada página.",
        "Una lectura obligada para los amantes de la literatura.",
        "No pude dejar de leerlo hasta terminarlo.",
        "Una narrativa cautivadora y personajes memorables.",
        "Una obra que te hace reflexionar sobre la vida.",
        "Recomendado para quienes disfrutan de la buena literatura."
    ]
    
    for libro in libros:
        # Crear entre 3 y 7 reseñas por libro
        num_resenas = random.randint(3, 7)
        for _ in range(num_resenas):
            # Calificación decimal entre 0.0 y 5.0
            calificacion = round(random.uniform(1.0, 5.0), 1)
            comentario = random.choice(comentarios)
            
            # Fecha de creación aleatoria en los últimos 30 días
            dias_atras = random.randint(1, 30)
            fecha_creacion = datetime.datetime.now() - datetime.timedelta(days=dias_atras)
            
            Resena.objects.create(
                libro=libro,
                calificacion=calificacion,
                comentario=comentario,
                fecha_creacion=fecha_creacion
            )
    
    print("Datos poblados exitosamente!")

if __name__ == "__main__":
    print("Iniciando script de población de datos...")
    poblar_datos()
    print("Población de datos completada!")
