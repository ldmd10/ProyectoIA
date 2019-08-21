from django.contrib import admin

# Register your models here.
from .models import Algoritmo
from .models import Entrenamiento
from .models import DatosPrueba

admin.site.register(Algoritmo)
admin.site.register(DatosPrueba)
admin.site.register(Entrenamiento)
