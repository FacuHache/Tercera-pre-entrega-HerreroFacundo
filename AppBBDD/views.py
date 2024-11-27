from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio_db(req):
    return render (req, 'index_db.html') 
# o va el index.html mismo del módulo views.py de la carpeta de ProyectoTerceraPreEntrega (?)
# talvez en esta view mande a la plantilla los formularios (?)

def fecha(req):
    return render(req, 'fecha.html')

def jugador(req):
    return render(req, 'jugador.html')

def equipo_titular1(req):
    return render(req, 'equipo_titular1.html')

def equipo_titular2(req):
    return render(req, 'equipo_titular2.html')

# debería ir render a la plantilla que corresponda a cada formulario (?)
# y HttpResponse en las views que no accedan a la Base de datos (?)