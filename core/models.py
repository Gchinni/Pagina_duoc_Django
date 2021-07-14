from django.db import models

# Create your models here.
 

class Contacto(models.Model):
	nombre = models.CharField(max_length=150)
	rut = models.CharField(max_length=12)
	correo = models.CharField(max_length=100)
	telefono = models.CharField(max_length=13, null=True)
	ciudad = models.CharField(max_length=50)
	mensaje = models.TextField()

	def __str__(self):
		return self.nombre


class Mascotas(models.Model):
	nombre_dueno = models.CharField(max_length=150)
	nombre_mascota = models.CharField(max_length=150)
	raza = models.CharField(max_length=12)
	edad = models.IntegerField()
	imagen = models.ImageField(upload_to="mascotas", null=True)
	detalles = models.TextField(null=True)

	def __str__(self):
		return self.nombre_dueno
