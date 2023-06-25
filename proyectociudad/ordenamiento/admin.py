from django.contrib import admin

# Register your models here.
from ordenamiento.models import Parroquia, Barrio

class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo')
    search_fields = ('nombre', 'tipo')

admin.site.register(Parroquia, ParroquiaAdmin)


class BarrioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nro_viviendas', 'nro_parques', 'nro_edificios', 'get_parroquia')
    search_fields = ('nombre', 'get_parroquia')
    raw_id_fields = ('parroquia',)

    def get_parroquia(self, obj):
        return obj.parroquia.nombre
    
admin.site.register(Barrio, BarrioAdmin)