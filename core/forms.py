from django import forms
from .models import Contacto, Mascotas

class ContactoForm(forms.ModelForm):

	nombre = forms.CharField(widget=forms.TextInput(attrs={"id":"nombre"}))
	rut = forms.CharField(widget=forms.TextInput(attrs={"id":"rut", "type":"tel"}))
	correo = forms.CharField(widget=forms.TextInput(attrs={"id":"correo", "type":"email"}))
	telefono = forms.CharField(widget=forms.TextInput(attrs={"value":"(opcional)"}))
	ciudad = forms.CharField(widget=forms.TextInput(attrs={"id":"ciudad"}))
	mensaje = forms.CharField(widget=forms.TextInput(attrs={"id":"mensaje"}))

	class Meta:
		model = Contacto
		#fields = ["nombre", "rut", "correo", "telefono", "ciudad", "mensaje"]
		fields = '__all__'

class MascotaForm(forms.ModelForm):

	class Meta:
		model = Mascotas
		fields = '__all__'


