"""
URL configuration for ProyectoTerceraPreEntrega project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ProyectoTerceraPreEntrega.views import saludo, ver_equipo_titular, ingresar_fecha_partido, faltan_x_dias, template_index, agregar_jugador, quitar_jugador # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo), #'''name='saludo' '''cual sería la función de name='saludo'??
# ya entendí que el name en el path es unico para que pueda ser llamado en el template,
# sería desde los 'template' 'plantillas' desde la carpeta 'Plantillas', o desde cualquier
# parte del proyecto?
# y creo que es para que Django lo pueda identificar en el template al momento ir a buscar
# la 'función' 'view' requerida
    path('ver_equipo_titular/', name ='ver_equipo_titular', view= ver_equipo_titular),
    path('ingresar_fecha_partido/', name = 'ingresar_fecha_partido', view= ingresar_fecha_partido),
    path('faltan_x_dias/', name = 'faltan_x_dias', view= faltan_x_dias),
    path('template_index/', name = 'template_index', view= template_index),
    path('agregar_jugador/', name = 'agregar_jugador', view= agregar_jugador),
    path('quitar_jugador/', name = 'quitar_jugador', view= quitar_jugador),
    #en minúscula:
#    path('INGRESAR_JUGADOR/', INGRESAR_JUGADOR), #esta ruta aún no existe en views.py
#    path('ACTUALIZAR_JUGADOR/', ACTUALIZAR_JUGADOR),
    
]
