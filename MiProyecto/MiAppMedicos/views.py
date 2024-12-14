# Create your views here.
from django.shortcuts import render
from .models import MedicoModels
from .forms import MedicoForm
import csv
import os
from MiAppMedicos.forms import MedicoForm

from django.http import HttpResponse

#def medico_view(request):
#    if request.method == 'POST':
 #       form = MedicoForm(request.POST)
 #       if form.is_valid():
 #           file_exists = os.path.isfile('medicos.csv')
 #           with open('medicos.csv', 'a', newline='') as file:
 #               writer = csv.writer(file)
 #               if not file_exists:
 #                   writer.writerow(['Nombre', 'Apellido', 'Matricula', 'Especialidad'])  # Escribir la cabecera
 #               writer.writerow([
 #                   form.cleaned_data['nombre'],
 #                   form.cleaned_data['apellido'],
 #                   form.cleaned_data['matricula'],
 #                   form.cleaned_data['profesion']
 #               ])
 #           form = MedicoForm()  # Resetear el formulario después de guardar
 #   else:
 #       form = MedicoForm()
    
 #   return render(request, 'MiAppMedicos/altamedico.html'), {'form': form}
 
 
def portada (request):
     return render(request, 'MiAppMedicos/medicos.html')
 
def AltaMedico (request):
     return render(request, 'MiAppMedicos/altamedico.html')     
 
 
 
from MiAppMedicos.forms import MedicoForm
 
def medico_view(request):
 
    if request.method == "POST":
 
            miFormulario = MedicoForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                medico = MedicoModels(nombre=informacion["nombre"], apellido=informacion["apellido"], matricula=informacion["matricula"], profesion=informacion["profesion"] )
                medico.save()
                return render(request, "MiAppMedicos/medicos.html")
    else:
            miFormulario = MedicoForm()
 
    return render(request, "MiAppMedicos/altamedico.html", {"miFormulario": miFormulario})
 