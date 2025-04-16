Sistema de Gestión de Biblioteca
Un sistema web simple para la gestión de libros, autores, categorías y editoriales desarrollado con Django.
Descripción
Este proyecto es una aplicación web para administrar una biblioteca, permitiendo gestionar libros, autores, categorías y editoriales. La aplicación facilita el registro, actualización, búsqueda y eliminación de estos recursos de manera eficiente.
Requisitos Previos

Python 3.8 o superior
pip (gestor de paquetes de Python)

Instalación

Clona este repositorio o descárgalo como ZIP

bashgit clone https://github.com/tu-usuario/sistema-biblioteca.git
cd sistema-biblioteca

Crea y activa un entorno virtual (recomendado)

bash# En Windows
python -m venv venv
venv\Scripts\activate

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate

Instala las dependencias

bashpip install -r requirements.txt

Realiza las migraciones de la base de datos

bashpython manage.py migrate

Crea un superusuario para acceder al panel de administración

bashpython manage.py createsuperuser

Inicia el servidor de desarrollo

bashpython manage.py runserver

Accede a la aplicación en tu navegador: http://127.0.0.1:8000/

Dependencias Principales

Django 4.2.20: Framework web de alto nivel para desarrollo rápido
Pillow 11.2.1: Biblioteca para el procesamiento de imágenes
Otras dependencias de soporte (asgiref, sqlparse, typing_extensions, tzdata)

Estructura de la Aplicación

Libros: Administración de libros con título, autor, ISBN, año de publicación, etc.
Autores: Gestión de información de autores
Categorías: Clasificación de libros por géneros o temáticas
Editoriales: Registro de editoriales y su información

Uso
Una vez que el servidor esté en funcionamiento, puedes:

Visitar la página principal para acceder a las diferentes secciones
Utilizar la barra de navegación para moverte entre libros, autores, categorías y editoriales
Usar el buscador para encontrar recursos específicos
Acceder al panel de administración en http://127.0.0.1:8000/admin/ (usando las credenciales del superusuario)
