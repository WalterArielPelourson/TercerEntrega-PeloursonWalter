from django.db import models

# Tabla Medicos
class MedicoModels(models.Model):
    
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    matricula = models.CharField(max_length=8)
    profesion = models.CharField(max_length=30)
    def __str__(self):
        return  f"{self.id} | Nombre: {self.nombre} | Apellido: {self.apellido} | Profesion: {self.profesion}"
    
    ()
#Tabla Clientes
class PacienteModels(models.Model):
    
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    obrasocial = models.CharField(max_length=8)
    edad = models.IntegerField()
    fechanacimiento = models.DateField()
    def __str__(self):
        return  f"{self.id} | Nombre: {self.nombre} | Apellido: {self.apellido} | Profesion: {self.obrasocial}"