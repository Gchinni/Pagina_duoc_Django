from django.urls import path
from .views import index, contacto, formulario, resultado, servicios, agregar_mascota, listar_mascota, modificar_mascota, eliminar_mascota, index_api


urlpatterns = [
    path('', index, name="index"),
    path('contacto/', contacto, name="contacto"),
    path('formulario/', formulario, name="formulario"),
    path('resultado/', resultado, name="resultado"),
    path('servicios/', servicios, name="servicios"),
    path('agregar/', agregar_mascota, name="agregar"),
    path('listar/', listar_mascota, name="listar"),
    path('modificar/<id>/', modificar_mascota, name="modificar"),
    path('eliminar/<id>/', eliminar_mascota, name='eliminar'),
    path('index-api/', index_api, name="index_api")

]