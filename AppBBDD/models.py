from django.db import models

# Create your models here.

# cuantos modelos necesito?

# ejemplos:
'''
# 1. modelo de usuario
# 2. modelo de producto
# 3. modelo de pedido
# 4. modelo de categoria
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='categorias')
    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        class Producto(models.Model):
            nombre = models.CharField(max_length=50)
'''
# Fechas de los partidos
class Fecha(models.Model):
    fecha = models.DateField()  
    resultado = models.CharField(max_length=20, default='pts equipo/pts rival')


# mostrará una lista de todos los jugadores del equipo
class Jugador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField(null=True)
    fecha_nacimiento = models.DateField()
    descripcion = models.TextField(default='ej, tipo de juego, habilidades, caracteristicas, condiciones')


# equipo titular
class Equipo_Titular(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField(null=True)
    estado_juega = models.BooleanField(default=True) # como setear este camo en la DB (pregunta)
    descripcion = models.TextField(default='ingresar del 1 - 10, como se encuentra/siente el jugador' )
    # (próximamente) imagen = models.ImageField(upload_to='equipos')