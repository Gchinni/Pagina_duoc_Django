from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactoForm, MascotaForm
from .models import Mascotas
# Create your views here.


def index(request):
	return render(request, 'core/index.html')

def servicios(request):
	return render(request, 'core/servicios.html')

def formulario(request):
	data = {
		'form': ContactoForm()
	}

	
	if request.method == 'POST':
		formulario = ContactoForm(data=request.POST)
		
		if formulario.is_valid():
			formulario.save()
			data["mensaje"] = "Contacto enviado"
		else:
			data["form"] = formulario
		
	
	return render(request, 'core/formulario.html', data)

def resultado(request):
	return render(request, 'core/resultado.html')

def contacto(request):
	return render(request, 'core/contacto.html')

def agregar_mascota(request):
	data = {
		'form': MascotaForm()
	}

	if request.method == 'POST':
		formulario = MascotaForm(data=request.POST, files=request.FILES)
		
		if formulario.is_valid():
			formulario.save()
			data["mensaje"] = "mascota agregada"
		else:
			data["form"] = formulario

	return render(request, 'core/mascota/agregar.html', data)

def listar_mascota(request):

	mascotas = Mascotas.objects.all()

	data = {
		'mascotas': mascotas
	}

	return render(request, 'core/mascota/listar.html', data)



def modificar_mascota(request, id):

	mascota = get_object_or_404(Mascotas, id=id)

	data= {
		'form' : MascotaForm(instance=mascota)
	}

	if request.method == 'POST':
		formulario = MascotaForm(data=request.POST, instance=mascota, files=request.FILES)
		
		if formulario.is_valid():
			formulario.save()
			return redirect(to="listar")
		else:
			data["form"] = formulario

	return render(request, 'core/mascota/modificar.html', data)

def eliminar_mascota(request, id):

	mascota = get_object_or_404(Mascotas, id=id)
	mascota.delete()
	return redirect(to="listar")
	
def index_api(request):
	return render(request, 'core/index-api.html')
