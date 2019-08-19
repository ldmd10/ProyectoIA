from django.db import models


# Create your models here.
class DataSet(models.Model):
    TIPO_DATA_IMAGEN = 'imagen'
    TIPO_DATA_REGLAS = 'reglas'
    TIPO_DATA_CLUSTER = 'cluster'
    TIPO_DATA_CLASIFICACIONID3 = 'clasificaciónid3'

    OPCIONES_TIPO_DATA = (
        (TIPO_DATA_REGLAS, 'Reglas'),
        (TIPO_DATA_CLUSTER, 'Cluster'),
        (TIPO_DATA_CLASIFICACIONID3, 'Clasificación-Id3'),
        (TIPO_DATA_IMAGEN, 'Imagen'),
    )

    idDataSet = models.AutoField(primary_key=True, null=False, max_length=10)
    nombreDataSet = models.CharField(max_length=30)
    tipoDataSet = models.CharField(max_length=40, verbose_name="Tipo datos", choices=OPCIONES_TIPO_DATA,
                                   default=TIPO_DATA_REGLAS)
    tamañoDataSet = models.IntegerField()
    claseDataSet = models.CharField(max_length=40, null=True, blank=True)

    datos = models.FileField(upload_to='Archivos/dataSet', null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.nombreDataSet)

    def getURL(self):
        urlDescarga = str(self.datos.path)
        return self.datos.name

    def getimagenes(self):
        img = []
        for imgData in self.imagendata_set:
            img.append(imgData)
        return img

    def dataArchivo(self):
        '''
        Este metodo lee el archivo y retorna una cadena con su contenido
        :return: cadena
        '''
        archivo = open(self.datos.name, "r")
        cadena = "\n"
        cadena = cadena + archivo.read()
        archivo.close()
        print("---------------")
        print(cadena)
        return cadena


class ImagenData(models.Model):
    clase = models.CharField(max_length=50)
    imagen = models.FileField(upload_to='Archivos/dataSet', null=True, blank=False)
    dataSet = models.ForeignKey(DataSet, on_delete=models.CASCADE)

    def __str__(self):
        return self.imagen.name
