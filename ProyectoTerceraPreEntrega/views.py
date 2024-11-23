from django.http import HttpResponse
#los siguientes 2 from son para el método de cuantos días faltan para la siguiente fecha
from datetime import date
from datetime import timedelta

#page ppal (agregar botones de inicio con las views opcionales, esto es para el inicio.)
#se harían los botones para cada una de las opciones
#es acá o en donde??
#POR LO QUE VEO LOS BOTONES PARA LAS VISTAS VAN EL MÓDULO INDEX.HTML
#Y PARECE QUE FALTA LA CARPETA "MI_APP" PARA DEFINIR EL INDEX.HTML AHÍ MISMO ruta:
#mi_app/templates/index.html (verificar) ! ! ! 
def index(request):
    return HttpResponse("parece que acá no va el index - Esta es la página principal")

#se podría agregar un button / método para ver el calendario
#esta función es para mostrar el calendario
'''def calendario(request):
    return render(request, 'calendario.html')'''

def saludo (request):
    return HttpResponse('Hola crack!')

#metodo n°1
#definiendo una segunda vista... esta podría asignarse a uno de los buttons de la página principal
def segunda_vista (request):
    return HttpResponse('Hola crack 2')

#método n°2: consultar estado del equipo titular para la proxima fecha
# definir una vista que reciba un parámetro

def ver_equipo_titular(request, fecha):
    #llamada a la base de datos
    #consultar estado del equipo titular para la proxima fecha
    return HttpResponse('Hola crack 3')


#método n°3: ingresar fechas de partidos a la DB
#definir una vista que reciba un parámetro
def ingresar_fecha_partido(request, fecha):
    #llamada a la base de datos
    #ingresar fechas de partidos a la DB
    #usar if o try except por si la fecha no existe o es mal ingresada
    return HttpResponse('Fecha ingresada') #'''así???'''

#método n°4: con la función date comparar y devolver cuantos días faltan para la proxima fecha de partido

#recibe un parámetro ingresado por usuario o consultado a la DB
def faltan_x_dias (request, fecha): 
    fecha_proxima = date(fecha) # ingresar en formato "2024, 3, 15" fecha de prox partido
    diferencia = fecha_proxima - date.today()
    return HttpResponse(f'Faltan {diferencia.days} días para el partido')
