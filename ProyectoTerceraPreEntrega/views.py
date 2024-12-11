from django.http import HttpResponse
#los siguientes 2 from son para el método de cuantos días faltan para la siguiente fecha
from datetime import date
from datetime import timedelta

#DEFINIENDO EL TEMPLATE (verificar que esté en la carpeta correcta, en el módulo correcto views)
# Agregamos al encabezado del archivo el import de Template y de Context
from django.template import Template, Context, loader



def template_index(request):
    '''
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
    '''
    diccionario = {}
    
    plantilla = loader.get_template('index.html')
    
    documento = plantilla.render(diccionario)
    
    return HttpResponse(documento)