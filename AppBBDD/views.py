from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from datetime import timedelta
from django.template import Template, Context, loader

# Create your views here.

#se podría agregar un button / método para ver el calendario
#esta función es para mostrar el calendario
'''def calendario(request):
    return render(request, 'calendario.html')'''

def saludo (request):
    return HttpResponse('Hola crack!')


#método n°1: consultar estado del equipo titular para la proxima fecha
# definir una vista que reciba un parámetro
# por donde recibe el parámetro, por url?
def ver_equipo_titular(request):
    #llamada a la base de datos
    #consultar estado del equipo titular para la proxima fecha
    return HttpResponse('Este es el equipo titular')


#método n°2: ingresar fechas de partidos a la DB
#definir una vista que reciba un parámetro
def ingresar_fecha_partido(request, fecha):
    #llamada a la base de datos
    #ingresar fechas de partidos a la DB
    #usar if o try except por si la fecha no existe o es mal ingresada
    return HttpResponse('Fecha ingresada') #'''así???'''

#método n°3: con la función date comparar y devolver cuantos días faltan para la proxima fecha de partido

#recibe un parámetro ingresado por usuario o consultado a la DB
def faltan_x_dias (request, fecha): 
    fecha_proxima = date(fecha) # ingresar en formato "2024, 3, 15" fecha de prox partido
    # o ver si se despliega automaticamente para elegir la fecha a ingresar
    diferencia = fecha_proxima - date.today()
    return HttpResponse(f'Faltan {diferencia.days} días para el partido')

def agregar_jugador (request):
    return HttpResponse('Jugador agregado')

def quitar_jugador (request):
    return HttpResponse('Jugador eliminado')