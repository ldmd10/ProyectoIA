from django.db import models
from Apps.dataSet.models import DataSet
from Apps.algoritmo.Clases.Kmeans import kmeans
from Apps.algoritmo.Clases.knn import knn
from Apps.algoritmo.Clases.Apriori import Apriori
from Apps.algoritmo.Clases.FpGrowth import fpGrowth
from Apps.algoritmo.Clases.id3.main import id3
from Apps.algoritmo.Clases.UtilsArchivos import leerDatos



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
    '''Esta clase va ser exlusiva para kmeans y knn o similares'''
    idEntrenamiento = models.AutoField(primary_key=True, null=False, max_length=10)
    tituloEntrenamiento = models.CharField(max_length=80, verbose_name="Titulo entrenamiento")
    foraneaAlgoritmo = models.ForeignKey(Algoritmo, null=True, on_delete=models.CASCADE, verbose_name="Algoritmo")
    foraneaDataSet = models.ForeignKey(DataSet, null=True, on_delete=models.CASCADE, verbose_name="DataSet")
    tiempoEntrenamiento = models.DurationField(null=True, verbose_name="Tiempo entrenamiento")
    k = models.IntegerField(null=True)

    def __str__(self):
        return '{}'.format(self.tituloEntrenamiento)

    def ejecutarAlgoritmo(self):
        if self.foraneaAlgoritmo.nombreAlgoritmo == "Kmeans":
            k = int(0 if self.k is None else self.k)
            datosInput = leerDatos(self.foraneaDataSet.datos.url)
            seguimiento, grupos = kmeans(datosInput, k)
            salida = "\n" + "k =" + str(
                k) + "\n" + seguimiento + "\n" + "--------------------------------------Grupos--------------------------------------" + "\n" + grupos
            return salida
        if self.foraneaAlgoritmo.nombreAlgoritmo == "Knn":
            k = int(0 if self.k is None else self.k)
            datosInput = leerDatos(self.foraneaDataSet.datos.url)
            salidaknn = knn(datosInput, k)
            return salidaknn


class AlgoritmoReglas(models.Model):
    minSuport = models.FloatField(null=True)
    minConfianza = models.FloatField(null=True)
    tamañoCondicion = models.IntegerField(null=True)
    tamañoPredicado = models.IntegerField(null=True)
    minimoFrecuencia = models.IntegerField(null=True)
    foraneaAlgoritmo = models.ForeignKey(Algoritmo, null=True, on_delete=models.CASCADE, verbose_name="Algoritmo")
    foraneaDataSet = models.ForeignKey(DataSet, null=True, on_delete=models.CASCADE, verbose_name="DataSet")
    tiempoEntrenamiento = models.DurationField(null=True, verbose_name="Tiempo entrenamiento")

    def ejecutarAlgoritmo(self):
        if self.foraneaAlgoritmo.nombreAlgoritmo == "Apriori":
            datosInput = leerDatos(self.foraneaDataSet.datos.url)
            print("---------------------")
            print(datosInput)
            salida = Apriori(datosInput)
            print(salida)
            return str(salida)
        if self.foraneaAlgoritmo.nombreAlgoritmo == "FpGrowth":
            datosInput = leerDatos(self.foraneaDataSet.datos.url)
            print("---------------------")
            print(datosInput)
            salida = fpGrowth(datosInput)
            print(salida)
            return str(salida)


class DatosPrueba(models.Model):
    clase = models.CharField(max_length=50)
    tituloDataTest = models.CharField(max_length=50)
    dato = models.FileField(upload_to='Archivos/Prueba', null=True, blank=False)

    def __str__(self):
        return self.tituloDataTest


class Id3(models.Model):
    foraneaAlgoritmo = models.ForeignKey(Algoritmo, null=True, on_delete=models.CASCADE)
    foraneaDataSet = models.ForeignKey(DataSet, null=True, on_delete=models.CASCADE, verbose_name="DataSet")
    tiempoEntrenamiento = models.DurationField(null=True, verbose_name="Tiempo entrenamiento")
    tiempoEjecucion = models.TimeField(null=True)
    entradaPrueba = models.ForeignKey(DatosPrueba, null=True, on_delete=models.CASCADE, verbose_name="Datos prueba")

    def ejecutarAlgoritmo(self):
        rutaEntrada = self.foraneaDataSet.datos.url
        entradaJson = leerDatos(self.entradaPrueba.dato.url)
        salida = id3(rutaEntrada, entradaJson)

        return "Datos entrenamiento" + "\n" + leerCsv(rutaEntrada) + "\n" + \
               " Datos prueba " + "\n" + str(entradaJson) + "\n" + \
               "Salida " + "\n" + str(salida)
