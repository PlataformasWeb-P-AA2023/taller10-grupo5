from django.shortcuts import render, redirect
from ordenamiento.models import *
from ordenamiento.forms import *

# Create your views here.
def index(request):
    parroquias = Parroquia.objects.all()
    dic = {'parroquias': parroquias}
    return render(request, 'index.html', dic)

def crear_parroquia(request):
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST)
        
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm()

    dic = {'form': formulario}
    return render(request, 'crearParroquia.html', dic)


def editar_parroquia(request, id):
    parroquia = Parroquia.objects.get(pk=id)

    if request.method=='POST':
        formulario = ParroquiaForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm(instance=parroquia)
    
    dic = {'form': formulario}
    return render(request, 'editarParroquia.html', dic)


def eliminar_parroquia(request, id):
    parroquia = Parroquia.objects.get(pk=id)
    parroquia.delete()
    return redirect(index)


def listar_barrios(request):
    barrios = Barrio.objects.all()
    dic = {'barrios': barrios}
    return render(request, 'listar_barrios.html', dic)


def crear_barrio(request):
    if request.method=='POST':
        formulario = BarrioForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm()
    
    dic = {'form': formulario}
    return render(request, 'crearBarrio.html', dic)


def editar_barrio(request, id):
    barrio = Barrio.objects.get(pk=id)
    
    if request.method=='POST':
        formulario = BarrioForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm(instance=barrio)
    
    dic = {'form': formulario}
    return render(request, 'editarBarrio.html', dic)


def eliminar_barrio(request, id):
    barrio = Barrio.objects.get(pk=id)
    barrio.delete()
    return redirect(index)


def crear_barrio_parroquia(request, id):
    parroquia = Parroquia.objects.get(pk=id)
    
    if request.method=='POST':
        formulario = BarrioParroquiaForm(parroquia, request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioParroquiaForm(parroquia)

    dic = {'form': formulario, 'parroquia': parroquia}
    return render(request, 'crearBarrioParroquia.html', dic)