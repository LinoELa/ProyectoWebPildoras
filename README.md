# ProyectoWebPildoras

# Video II 
1. Empezamos con las vistas 
Home , servicios , tienda , blog contacto

2. vamos a URLs he importamos las vistas
En las vistas poner el singular el nombre de la url a buscar
    ==> path('servicios', views.servicios, name='Servicios'),


# Video III

Vamos a trabajar con URLs y Templates 

Un proyecto en django puede tener varias aplicacines 

1. Parte I
-> Una apliacion puede tener varios y se puede usar varias veces en varios proyecto.

-> Creamos una archivo url para unicamente nuesta apliacion 


-> Enlazamos URLs del proyecto en general con URLs de solo la aplicacion 

Despues de la configracion hay que reiniciar el servidor 


--> RENDERIZAR 

ahora solo nos devuelve un texto en la pantalla , 
perpo si queremos que renderize y no  devuelva un pagina HTML pues creamos una carpeta que plantillas : Templates

--> Esctrucutra basica de un HTML <-- 

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>

--> Esctrucutra basica de un HTML <-- 


2. Parte II

Vamos a settings.py para registrar nuestra aplicacion

3. ir a Views para renderizar las paginas dentro de las funciones. 
    ==> return render(request, 'ProyectoWebApp/home.html') ('Home')




# Video IV
1.  Apliacar formato a nuestro sitio web con BOOTSTRAP
2. Creacion de plantillas (Templates)
3. Herencias de plantillas y estrucutras del sitio

BOOTSTRAP : Es un framework CSS creado po Twitter n 2011
-> Es compatible con todos los dispositivos
-> Se utiliza mucho en CMS y WordPress


1. Crear una carpeta : STATIC  dentro crear una carpeta del proyecto : ProyectoWebApp


Tenemos que crear una plantilla base.


# Video V 

--> No hace falta incluir <!DOCTYPE html> 

1.  Creamos las plantillas 

a. tenemos que cargar los conntenidos de la carpeta STATIC

--> ENTENDER BIEN LOS ESTILOS DE BOOTSTRAP <-- 

-> despues de cargarlo todo para que funcione tengo que parar  el servidor y luego ponerlomas en marcha

-> En la pagina de css/gestion.css estan los estilos de la pagina home.


2.  HERENCIAS 

copiar la plantilla home.html y usarla como la plantilla padre.


Hemos usado home par que tengo  herede del padre 

-> {% extends "ProyectoWebApp/base.html" %}
        Tiene que ir arriba de todo, lo primero es como un import 

--> Home.html esta usado herencia de plantillas.

--> Hacer lo mismo las demas pero desde la base.html

Antes : 
      <a class="navbar-brand text-uppercase text-expanded font-weight-bold d-lg-none" href="home.html">Gestión de Pedidos</a>

Despues o Ahora : sin .html
      <a class="navbar-brand text-uppercase text-expanded font-weight-bold d-lg-none" href="{% url 'Home' %}">Gestión de Pedidos</a>

Asi con todas las demas url de base

--> Tengo que ponerlo con la primera letra en mayuscula como en el archivo URLs.py de ProyectoWebApp

    path('', views.home, name='Home'),

    path('servicios', views.servicios, name='Servicios'),



==> 

# VIDEO VI
-> COMPLETAR EL RESTO DE LAS PAGINAS CON LA HERENCIA DE PLANTILLAS

--> Hemos completado el header y footer y han tenido una herencia de base.html
-> Hemos puesto que se ilummina el menu en la seccion que nos encontramos en este momento 



# VIDEO VII

. VAMOS A CREAR UNA APP INDEPENDIENDE PARA LA ZONA DE SERVICIOS 
. La primera app (ProyectoWeb) hera como para poner las bases del proyecto ( es una parte del puzle )



Una app independiende 


1.  Creamos la app 
==> python manage.py startapp servicios

2. Registramos la app creado en nuestro archivo setting.py del proyecto generar que ser seria en (proyectoWeb - setting.py)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ProyectoWebApp',
    'servicios',
]


Django utiliza un mapeo ORM a la hora de utilizar las tablas 

--> Es utilizar la POO para manejar tablas y objetos que vendrian siendo tablas.


hemos usado models.py en casi todo 