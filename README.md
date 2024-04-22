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


