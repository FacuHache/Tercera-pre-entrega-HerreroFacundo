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
from django.urls import path, include
from ProyectoTerceraPreEntrega.views import template_index
# from ProyectoTerceraPreEntrega.views import saludo, ver_equipo_titular, ingresar_fecha_partido, faltan_x_dias, template_index, agregar_jugador, quitar_jugador # type: ignore
# esta es otra forma de importar las views, from al archivo views import view_1, view_2, etc
from AppBBDD import urls, views

urlpatterns = [
    path('', template_index, name='index'),
    # OJO OJO ! cuando pases las views de acá a AppBBDD.views,
    # que el archivo index.html va a quedar en la carpeta Plantillas del
    # ProyectoPrincipal 'ProyectoTerceraPreEntrega'
    # este path también hay que mandarlo a AppBDD.urls ???
    # o al ser la página de inicio puede o debe quedar donde está ¿
    path('admin/', admin.site.urls),
    path('AppBBDD/', include('AppBBDD.urls')),
]
