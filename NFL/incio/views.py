from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404

from .models import Equipos, Jugadores, Estadio
from .forms import CrearFormularioEquipos, CrearFormularioJugadores, CrearFormularioEstadio

def NFLInicio(request):
    equipos = Equipos.objects.all()
    jugadores = Jugadores.objects.all()
    estadios = Estadio.objects.all()
    return render(request, 'Inicio.html', {'equipos': equipos, 'jugadores': jugadores, 'estadios': estadios})

def crear(request):
    if request.method=='GET':
         return render(request,'crear.html',{
        'form': CrearFormularioJugadores
    })
    else:
        try:

            formVar=CrearFormularioJugadores(request.POST)
            formVar.save() 
            return redirect('/')
        except ValueError:
           return render (request,'crear.html', {
        'form': CrearFormularioJugadores,
        'error':'Porfavor envia datos validos'
    }) 
def modificar_equipos(request, id):
    try:
        identificarJugadores = get_object_or_404(jugadores, id=id)
    except Jugadores.DoesNotExist:
        raise Http404("El Jugador no fue encontrado") 

    data = {
        'form': CrearFormularioJugadores(instance=identificarJugadores)
    }

    if request.method == 'POST':
        formularioNuevo = CrearFormularioJugadores(data=request.POST, instance=identificaJugadores)
        if formularioNuevo.is_valid():
            formularioNuevo.save()
            data['mensaje'] = "Modificado correctamente"
            data['form'] = formularioNuevo
            
            return redirect('/')

    return render(request, 'editar.html', data)

def eliminar(request, id):
    eliminaR=get_object_or_404(jugadores,id=id)
    eliminaR.delete()
    return redirect('/')