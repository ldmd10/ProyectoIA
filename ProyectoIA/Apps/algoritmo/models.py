from django.db import models
from Apps.dataSet.models import DataSet


# Create your models here.
class Algoritmo(models.Model):
    # idAlgoritmo = models.AutoField(primary_key=True, null=False, max_length=10)

    TIPO_ALG_SUPERVISADO = 'supervisado'
    TIPO_ALG_NO_SUPERVISADO = 'no supervisado'

    OPCIONES_TIPO_ALG = (
        (TIPO_ALG_SUPERVISADO, 'Supervisado'),
        (TIPO_ALG_NO_SUPERVISADO, 'No supervisado'),
    )

    nombreAlgoritmo = models.CharField(max_length=200, null=True, verbose_name="Nombre algoritmo")
    tipo = models.CharField(max_length=100, choices=OPCIONES_TIPO_ALG, default=TIPO_ALG_NO_SUPERVISADO)
    descripcion = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return '{}'.format(self.nombreAlgoritmo)

    def ejecutarAlgoritmo(self):
        print("Corriendo algoritmo...")

    def entrenarAlgoritmo(self):
        print("Entrenando algoritmo..")

    def algoritmo1(self):
        print()

    def algoritmo2(self):
        print()

    def algoritmo3(self):
        print()

    def algoritmo4(self):
        print()

    def algoritmo5(self):
        print()

    def algoritmo6(self):
        print()


class Entrenamiento(models.Model):
    idEntrenamiento = models.AutoField(primary_key=True, null=False, max_length=10)
    tituloEntrenamiento = models.CharField(max_length=80, verbose_name="Titulo entrenamiento")
    foraneaAlgoritmo = models.ForeignKey(Algoritmo, null=False, on_delete=models.CASCADE, verbose_name="Algoritmo")
    foraneaDataSet = models.ForeignKey(DataSet, null=True, on_delete=models.CASCADE, verbose_name="DataSet")
    tiempoEntrenamiento = models.TimeField(null=True, verbose_name="Tiempo entrenamiento")

    def __str__(self):
        return '{}'.format(self.tituloEntrenamiento)


class Ejecucion(models.Model):
    idEjecucion = models.AutoField(primary_key=True, max_length=10)
    tituloEjecucion = models.CharField(max_length=80)
    foraneaAlgoritmo = models.ForeignKey(Algoritmo, null=True, on_delete=models.CASCADE)
    foraneaEntrenamiento = models.ForeignKey(Entrenamiento, null=True, on_delete=models.CASCADE)
    datoPrueba = models.FileField(upload_to='Archivos/Prueba', null=True, blank=False)
    tiempoEjecucion = models.TimeField(null=False)

    def __str__(self):
        return '{}'.format(self.tituloEjecucion)
