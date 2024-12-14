from django import forms

class MedicoForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    matricula = forms.CharField(max_length=8)
    profesion = forms.CharField(max_length=9)                            
                                 
                                
class PacienteForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    obrasocial = forms.CharField(max_length=8)
    edad = forms.IntegerField()
