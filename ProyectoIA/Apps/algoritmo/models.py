from django.db import models


# Create your models here.
class Algoritmo(models.Model):
    nombreAlgoritmo = models.CharField(max_length=200, null=True, blank=True)
    tipo = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.nombreAlgoritmo)

    def ejecutarAlgoritmo(self):
        print("Corriendo algoritmo...")

    def entrenarAlgoritmo(self):
        print("Entrenando algoritmo..")


class Entrenamiento(models.Model):
    idEntrenamiento = models.AutoField(primary_key=True,null=False, max_length=10)
    tituloEntrenamiento = models.CharField(max_length=80)
    foraneaAlgoritmo = models.ForeignKey(Algoritmo, null=False, on_delete=models.CASCADE)


class Ejecucion(models.Model):
    idEjecucion=models.AutoField(primary_key=True,max_length=10)
    tituloEjecucion=models.CharField(max_length=80)
    foraneaAlgoritmo = models.ForeignKey(Algoritmo, null=True, on_delete=models.CASCADE)
    foraneaEntrenamiento = models.ForeignKey(Entrenamiento, null=True, on_delete=models.CASCADE)
    datoPrueba=models.FileField(upload_to='Archivos/Test', null=False, blank=False)
    tiempoEjecucion=models.TimeField(null=False)

