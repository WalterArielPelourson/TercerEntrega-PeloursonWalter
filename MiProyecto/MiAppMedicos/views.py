# Create your views here.
from django.shortcuts import render, redirect
from .models import MedicoModels
from .models import PacienteModels
from .forms import MedicoForm
import csv
import os
from MiAppMedicos.forms import MedicoForm
from MiAppMedicos.forms import PacienteForm
from django.http import HttpResponse
from django.utils import timezone
from .models import Turno
from .forms import TurnoForm
from .forms import ConsultaForm

 
def portada (request):
     return render(request, 'MiAppMedicos/medicos.html')
 
def AltaMedico (request):
     return render(request, 'MiAppMedicos/altamedico.html')     
 
 
def medico_view(request):
 
    if request.method == "POST":
 
            miFormulario = MedicoForm(request.POST) # Aqui me llega la informacion del html
          
 
            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                medico = MedicoModels(nombre=informacion["nombre"], apellido=informacion["apellido"], matricula=informacion["matricula"], profesion=informacion["profesion"] )
                medico.save()
                return render(request, "MiAppMedicos/medicos.html")
    else:
            miFormulario = MedicoForm()
 
    return render(request, "MiAppMedicos/altamedico.html", {"miFormulario": miFormulario})
 
 
def paciente_view(request):
 
    if request.method == "POST":
            miformulario = PacienteForm(request.POST) # Aqui me llega la informacion del html
       
            if miformulario.is_valid():
                informacion = miformulario.cleaned_data
                paciente = PacienteModels(nombre=informacion["nombre"], apellido=informacion["apellido"], obrasocial=informacion["obrasocial"], edad=informacion["edad" ])
                paciente.save()
                return render(request, "MiAppMedicos/medicos.html")
    else:
            miformulario = PacienteForm()
 
    return render(request, "MiAppMedicos/altapaciente.html", {"miformulario": miformulario})



#Turnos

def cargar_turno(request):
    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"MiAppMedicos/medicos.html")
    else:
        form = TurnoForm()
    return render(request, 'MiAppMedicos/cargar_turno.html', {'form': form})


#Consulta Turnos
#def consultar_turnos1(request):
 #   hoy = timezone.now().date()
 #   turnos = Turno.objects.filter(fecha=hoy)
 #   return render(request, 'consultar_turnos.html', {'turnos': turnos})

def consultar_turnos(request):
    if request.method == 'POST':
        form1 = ConsultaForm(request.POST)
        if form1.is_valid():
            informacion = form1.cleaned_data
           
            turnos = Turno.objects.filter(fecha__icontains=informacion ["fecha"])
            
            return render(request,"MiAppMedicos/resultado_consultar.html", {"turnos": turnos})
    else:
        form1 = ConsultaForm()
    return render(request, 'MiAppMedicos/consultar_turnos.html', {'form1': form1})