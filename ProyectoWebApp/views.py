from django.shortcuts import render , HttpResponse

# para que se vea las fotos en servicios -----------
from servicios.models import Servicios


# Create your views here.

def home(request):
    return render(request, 'ProyectoWebApp/home.html')

def servicios(request):
    servicios = Servicios.objects.all()
    return render(request, 'ProyectoWebApp/servicios.html', {"servicios" : servicios}) 

def tienda(request):
    return render(request, 'ProyectoWebApp/tienda.html') 

def blog(request):
    return render(request, 'ProyectoWebApp/blog.html')

def contacto(request):
    return render(request, 'ProyectoWebApp/contacto.html') 