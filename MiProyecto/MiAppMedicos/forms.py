from django import forms

class MedicoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    matricula = forms.CharField(max_length=50)
    profesion = forms.CharField(max_length=100)
