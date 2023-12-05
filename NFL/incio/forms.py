from django.forms import ModelForm
from .models import  Equipos, Jugadores, Estadio


class CrearFormularioEquipos(ModelForm):
    class Meta:
        model=Equipos
        fields=['name']

class CrearFormularioJugadores(ModelForm):
    class Meta:
        model=Jugadores
        fields=['name']

class CrearFormularioEstadio(ModelForm):
    class Meta:
        model=Estadio
    
        fields=['name']