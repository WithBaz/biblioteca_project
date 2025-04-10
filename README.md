### Biblioteca Project

Sistema de gestión de biblioteca desarrollado con Django que permite administrar autores, libros y reseñas.

## Requisitos

- Python 3.8+
- Django


## Instalación rápida

```shellscript
# Clonar el repositorio
git clone https://github.com/tu-usuario/biblioteca_project.git
cd biblioteca_project

# Crear y activar entorno virtual (opcional)
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Instalar Django
pip install django

# Aplicar migraciones
python manage.py makemigrations
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser
```


## Poblar la base de datos

Para cargar datos de prueba:

```shellscript
python poblar_datos.py
```

## Ejecutar el servidor

```shellscript
python manage.py runserver
```

Accede al panel de administración en: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Modelos

- **Autor**: Nombre, biografía y fecha de nacimiento
- **Libro**: Título, autor, resumen y fecha de publicación
- **Reseña**: Libro, calificación (1-5), comentario y fecha de creación


## Operaciones CRUD

Todas las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) se realizan a través del panel de administración de Django.

## Validaciones

- El nombre del autor no puede estar vacío o contener solo espacios
- El resumen del libro debe tener al menos 50 caracteres
- La calificación de la reseña debe estar entre 1 y 5
