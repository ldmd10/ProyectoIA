from django.db import models

# Create your models here.
class Algoritmo(models.Model):
    nombreAlgoritmo=models.CharField(max_length=200)