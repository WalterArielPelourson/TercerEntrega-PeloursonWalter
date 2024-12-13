from django.contrib import admin # type: ignore
from MiAppMedicos.models import MedicoModels
from MiAppMedicos.models import PacienteModels

# Register your models here.

admin.site.register(MedicoModels)
admin.site.register(PacienteModels)

