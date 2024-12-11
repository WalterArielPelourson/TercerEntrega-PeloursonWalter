# Create your views here.
from django.shortcuts import render
from .models import MedicoModels
from .forms import MedicoForm
import csv

from django.http import HttpResponse

def medico_view(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            with open('medicos.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([
                    form.cleaned_data['nombre'],
                    form.cleaned_data['apellido'],
                    form.cleaned_data['matricula'],
                    form.cleaned_data['profesion']
                ])
            form = MedicoForm()  # Reset the form after saving
    else:
        form = MedicoForm()

    return HttpResponse(medico_view)
    
    #return render(request, 'templates.html', {'form': form})
    #return render(request, 'medico_form.html', {'form': form})
 