from django.contrib import admin

# Register your models here.
from .models import Algoritmo, Ejecucion
from .models import Entrenamiento

admin.site.register(Algoritmo)
admin.site.register(Entrenamiento)
admin.site.register(Ejecucion)
