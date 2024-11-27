from django.urls import path
from AppBBDD import views
#probando si se pueden importar las vistas como en urls.py de la carpeta 'ProyectoTerceraPreEntrega/urls.py':
from AppBBDD.views import inicio_db, fecha, jugador, equipo_titular1, equipo_titular2

urlpatterns = [
    path('inicio_db/', inicio_db),
    # ver si se puede hacer lo siguiente y que no se pise con la direccion de
    # 'inicio' en urls.py de la carpeta 'ProyectoTerceraPreEntrega/urls.py':
    
    # path('', template_index, name='inicio'),
    path('fecha/', fecha),
    path('jugador/', jugador),
    path('equipo_titular1/', equipo_titular1),
    path('equipo_titular2/', equipo_titular2),
    
    # puede ser que a los paths les falte el nombre (único para ser llamado), ¿pero no es necesario?
    
]