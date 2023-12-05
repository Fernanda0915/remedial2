from django.contrib import admin

from .models import Equipos
from .models import Jugadores
from .models import Estadio



@admin.register(Equipos)
class EquiposAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'evento', 'NombreDueño']

@admin.register(Jugadores)  
class JugadoresAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'numero', 'posicion'] 

@admin.register(Estadio)
class EstadioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'capacidad', 'tamaño']