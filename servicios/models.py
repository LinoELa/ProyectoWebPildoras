from django.db import models

# Create your models here.


class Servicios (models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField() #instalar : -> "python -m pip install Pillow". <-
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    # Para crear su  representacion en la base de datos 
    class Meta :
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'


    def __str__(self):
        return self.titulo
    

    # 1. al completarlo tenemos que hacer un makemigrations
            #==> python manage.py makemigrations

    # 2. hacermos una migracion
            #==> python manage.py migrate

                    #para saber si ha funcionado mirar si se ha credo la tablas en la base de datos.
    
