from django.http import HttpResponse
#los siguientes 2 from son para el método de cuantos días faltan para la siguiente fecha
from datetime import date
from datetime import timedelta

#DEFINIENDO EL TEMPLATE (verificar que esté en la carpeta correcta, en el módulo correcto views)
# Agregamos al encabezado del archivo el import de Template y de Context
from django.template import Template, Context

#page ppal (agregar botones de inicio con las views opcionales, esto es para el inicio.)
#se harían los botones para cada una de las opciones
#es acá o en donde??
#POR LO QUE VEO LOS BOTONES PARA LAS VISTAS VAN EL MÓDULO INDEX.HTML
#Y PARECE QUE FALTA LA CARPETA "MI_APP" PARA DEFINIR EL INDEX.HTML AHÍ MISMO ruta:
#mi_app/templates/index.html (verificar) ! ! ! 
def index(request):
    return HttpResponse("parece que acá no va el index - Esta es la página principal? es el index.html creado en la raíz?")

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

def ver_equipo_titular(request):
    #llamada a la base de datos
    #consultar estado del equipo titular para la proxima fecha
    return HttpResponse('Este es el equipo titular')


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
    # o ver si se despliega automaticamente para elegir la fecha a ingresar
    diferencia = fecha_proxima - date.today()
    return HttpResponse(f'Faltan {diferencia.days} días para el partido')

def agregar_jugador (request):
    return HttpResponse('Jugador agregado')

def quitar_jugador (request):
    return HttpResponse('Jugador eliminado')

def template_index(request):

    # Abrimos el archivo html
    mi_html = open('.\ProyectoTerceraPreEntrega\Plantillas\index.html')

    # Creamos el template haciendo uso de la clase Template
    plantilla = Template(mi_html.read())

    # Cerramos el archivo previamente abierto, ya que lo tenemos cargado en la variable plantilla
    mi_html.close()

    # Creamos un contexto, más adelante vamos a aprender a usarlo, ahora lo necesitamos aunque sea vacío para que funcione
    mi_contexto = Context()

    # Terminamos de construír el template renderizándolo con su contexto
    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)