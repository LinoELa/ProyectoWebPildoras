
# URLs.py de  unicamente nuestra aplicacion 

from django.urls import path

from ProyectoWebApp import views

# Registrar URL para las fotos (importar ) ------------
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    # lo eliminamos (path(admin) porque no hay
    path('', views.home, name='Home'),
    path('servicios', views.servicios, name='Servicios'),
    path('tienda', views.tienda, name='Tienda'),
    path('blog', views.blog, name='Blog'),
    path('contacto', views.contacto, name='Contacto'),
]

# Registrar URL para las fotos  ------------

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )