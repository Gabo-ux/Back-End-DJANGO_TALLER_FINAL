from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect, render
from CRUD.forms import Forminscripcion
from CRUD.models import Inscripciones

# Create your views here.

def index(request):
    return render(request, 'index.html')

def listar_Inscripciones(request):
    ins = Inscripciones.objects.all()
    data = {'inscripcion': ins}
    return render(request, 'listar_inscripciones.html', data)

def agregar_inscripcion(request):
    form = Forminscripcion()
    if request.method == 'POST':
        form = Forminscripcion(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregar_inscripcion.html', data)

def eliminar_inscripcion(request, id):
    ins = Inscripciones.objects.get(id = id)
    ins.delete()
    return redirect(request, '/CRUD_listar_inscripcion')

def actualizar_inscripcion(request, id):
    ins = Inscripciones.objects.get(id = id)
    form = Forminscripcion(instance=ins)
    if request.method == 'POST':
        form = Forminscripcion(request.POST, instance=ins)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'agregar_inscripcion.html', data)