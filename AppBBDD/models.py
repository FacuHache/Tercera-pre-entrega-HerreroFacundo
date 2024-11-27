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
# Fechas
class Fecha(models.Model):
    fecha = models.DateField()  
    class Meta:
        verbose_name = 'fecha'
        verbose_name_plural = 'fechas'
        ordering = ['fecha']

# Jugador
class Jugador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    class Meta:
        verbose_name = 'jugador'
        verbose_name_plural = 'jugadores'
        ordering = ['nombre']  # Ordenar por el campo 'nombre'


# equipo titular OP 1
# debería estar relacionado con el jugador
class Equipo_Titular(models.Model):
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    fecha = models.ForeignKey(Fecha, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'equipo titular'
        verbose_name_plural = 'equipos titulares'
        #ordenar por nombre de jugador
        ordering = ['jugador.nombre'] # verificar que el campo exista para ordenar correctamente

# equipo titular OP 2
class Equipo_Titular(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    # imagen = models.ImageField(upload_to='equipos')
    class Meta:
        verbose_name = 'equipo titular'
        verbose_name_plural = 'equipos titulares'
        ordering = ['nombre'] # debería ordenar por nombre de Jugador