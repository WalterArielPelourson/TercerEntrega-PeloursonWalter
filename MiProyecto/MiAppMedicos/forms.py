from django import forms

class MedicoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    matricula = forms.CharField(max_length=50)
    profesion = forms.CharField(max_length=100)


#class PacienteForm(forms.Form):
#    nombre = forms.CharField(max_length=20)
 #   apellido = forms.CharField(max_length=20)
#    obrasocial = forms.CharField(max_length=8)
#    edad = forms.IntegerField()
 #   fechanacimiento = forms.DateField()