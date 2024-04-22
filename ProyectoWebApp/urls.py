
# URLs.py de  unicamente nuestra aplicacion 

from django.urls import path

from ProyectoWebApp import views

urlpatterns = [
    # lo eliminamos (path(admin) porque no hay
    path('', views.home, name='Home'),
    path('servicios', views.servicios, name='Servicios'),
    path('tienda', views.tienda, name='Tienda'),
    path('blog', views.blog, name='Blog'),
    path('contacto', views.contacto, name='Contacto'),
]