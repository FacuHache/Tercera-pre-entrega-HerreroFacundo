from django.urls import path
from AppBBDD import views

urlpatterns = [
    path('saludo/', views.saludo, name= 'saludo'), #'''name='saludo' '''cual sería la función de name='saludo'??
# ya entendí que el name en el path es unico para que pueda ser llamado en el template,
# sería desde los 'template' 'plantillas' desde la carpeta 'Plantillas', o desde cualquier
# parte del proyecto?
# y creo que es para que Django lo pueda identificar en el template al momento ir a buscar
# la 'función' 'view' requerida
    path('ver_equipo_titular/', views.ver_equipo_titular, name= 'ver_equipo_titular'),
    path('ingresar_fecha_partido/', views.ingresar_fecha_partido, name= 'ingresar_fecha_partido'),
    path('faltan_x_dias/',  views.faltan_x_dias, name= 'faltan_x_dias'),
    path('agregar_jugador/',  views.agregar_jugador, name= 'agregar_jugador'),
    path('quitar_jugador/', views.quitar_jugador, name= 'quitar_jugador'),

]
