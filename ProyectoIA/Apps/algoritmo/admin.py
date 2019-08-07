from django.contrib import admin

# Register your models here.
from .models import Algoritmo
from  .models import Entrenamiento

admin.site.register(Algoritmo)
admin.site.register(Entrenamiento)
