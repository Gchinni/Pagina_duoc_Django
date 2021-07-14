from django.contrib import admin
from .models import Contacto, Mascotas

# Register your models here.


class MascotaAdmin(admin.ModelAdmin):
	list_display = ["nombre_dueno", "nombre_mascota", "raza", "edad"]
	search_fields = ["nombre_dueno"]
	list_filter = ["nombre_dueno", "nombre_mascota"]
	list_per_page = 5



admin.site.register(Contacto)
admin.site.register(Mascotas, MascotaAdmin)