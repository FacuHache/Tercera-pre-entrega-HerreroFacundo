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
from ProyectoTerceraPreEntrega.views import saludo, ver_equipo_titular, ingresar_fecha_partido, faltan_x_dias, template_index, agregar_jugador, quitar_jugador

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo), #'''name='saludo' '''cual sería la función de name='saludo'??
    path('ver_equipo_titular/', ver_equipo_titular),
    path('ingresar_fecha_partido/', ingresar_fecha_partido),
    path('faltan_x_dias/', faltan_x_dias),
    path('template_index/', template_index),
    path('agregar_jugador/', agregar_jugador),
    path('quitar_jugador/', quitar_jugador),
    #en minúscula:
#    path('INGRESAR_JUGADOR/', INGRESAR_JUGADOR), #esta ruta aún no existe en views.py
#    path('ACTUALIZAR_JUGADOR/', ACTUALIZAR_JUGADOR),
    
]
