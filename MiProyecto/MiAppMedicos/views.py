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
from .models import MedicoModels
from .forms import TurnoForm
from .forms import ConsultaForm
from django.views.generic import ListView


 
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
                return render(request, "MiAppMedicos/TempBaseCargaDatos.html")
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
                return render(request, "MiAppMedicos/TempBaseCargaDatos.html")
    else:
            miformulario = PacienteForm()
 
    return render(request, "MiAppMedicos/altapaciente.html", {"miformulario": miformulario})



#Turnos

def cargar_turno(request):
    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"MiAppMedicos/TempBaseCargaDatos.html")
    else:
        form = TurnoForm()
    return render(request, 'MiAppMedicos/cargar_turno.html', {'form': form})




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



class MedicoModelsListView(ListView):
    model = MedicoModels
    context_object_name = "MBMedicos"
    template_name = "MiAppMedicos/BMMedicos.html"
    


#Borrar Medico
def borramedico(request, MedicoModels_id):
    try:
        borra = MedicoModels.objects.get(id=MedicoModels_id)
    except MedicoModels.DoesNotExist:
        return render(request,"MiAppMedicos/medicos.html")
    borra.delete()
    return render(request, "MiAppMedicos/TempBaseCargaDatos.html")   


#Edita Medico
def editamedico(request, MedicoModels_id):
    try:
        edita = MedicoModels.objects.get(id=MedicoModels_id)
    except MedicoModels.DoesNotExist:
        return render(request,"MiAppMedicos/medicos.html")
    if request.method == "POST":
        formulario = MedicoForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            edita.nombre = data["nombre"]
            edita.apellido = data["apellido"]
            edita.matricula = data["matricula"]
            edita.profesion = data["profesion"]
            edita.save()
            return render(request, "MiAppMedicos/TempBaseCargaDatos.html")
            
        
    formulario = MedicoForm(
        initial = {
            "nombre": edita.nombre,
            "apellido": edita.apellido,
            "matricula": edita.matricula,
            "profesion": edita.profesion,       
        } 
    )
    return render(request, "MiAppMedicos/edita_medico.html", {"form": formulario})