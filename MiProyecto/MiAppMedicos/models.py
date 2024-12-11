from django.db import models

# Create your models here.
class MedicoModels(models.Model):
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    matricula = models.CharField(max_length=50)
    profesion = models.CharField(max_length=100)