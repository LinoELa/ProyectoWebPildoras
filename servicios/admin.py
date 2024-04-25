from django.contrib import admin
from .models import Servicios

# Register your models here.
#AHORA TENEOS QUE REGISTRAS NUESTA APLIACION SE Servicios
# ya dimos de alta en el archivo models.


class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') #es decirle que solo  lea estas clases 

admin.site.register(Servicios, ServicioAdmin)


