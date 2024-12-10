Esta es la página de un equipo de interclubes de tenis.

El equipo se llama "Los Tenistas de la Costa"
El equipo tiene 5 jugadores titulares por fecha

La idea inicial es que la página fuese bastante intuitiva y toda la información que necesitan para navegar
en cada view se vea por pantalla

o al menos esa era la idea. Cómo claramente no se llegó a terminar las funcionalidades
 de la página aquí encontrarán las acciones en funcionamiento:

(a completar)

funciones:
-------	VER EQUIPO TITULAR
			* mostrará los jugadores definidos para la próxima fecha, sino 
				'Aún no hay jugadores definidos'
				# ordering apellido
			* agregar jugador
			* quitar jugador


-------	VER JUGADORES
			* buscar jugador (mostrará datos atributos del jugador, sino 'no existe el 					jugador o ingresar correctamente el parámetro filtro dato 					por el cual buscar)
			* agregar jugador 
			* quitar jugador


-------	VER FECHAS
		* mostrará las fechas ingresadas hasta ahora
		* la fecha actual
		* la próxima fecha, si no hay fecha = null
		* cuantos días faltan para la próxima fecha, sino hay fechas null
		* ingresar fecha
		* borrar fecha
		
	
	
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


*-crear AppBBDD con StartApp / startProyect
*- definir models.py con las 3 Clases para que sean la DB
	+ asociar la AppBBDD en setings.y en la carpeta ppal del proyecto
	+ codear include e importarlo en 'urls.py /foldes ppal' para que reconozca los paths y las 		views de de la carpeta de la AppBBDD
	+ 

* definir la url de inicio para que muestre directamente el template de inicio con los botones
* crear formularios para cada model / Clase en AppBBDD/models.py
* crear BBDD con los comandos makemigratio, migrate, etc



@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



hacer:
* corregir los parámetros de los modelos por CharFields etc (listo)
* verificar DB y por qué no funka el include (listo)
* plantilla template, para ingresar fecha
* qué otra plantilla falta(?)
* template o view para mostrar los días que faltan para el prox partido
* hacer DB del equipo titular (faltan ingresar valores a la planilla)
* formulario para ingresar jugador al equipo titular
* formulario para quitar jugador del equipo titular (mostrando en ese template los jugadores actuales)
* codear los módulos.html de la carpeta 'AppBBDD' (modelar los templates de la DB?)