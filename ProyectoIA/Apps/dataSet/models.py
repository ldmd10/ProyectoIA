from django.db import models


# Create your models here.
class DataSet(models.Model):
    TIPO_DATA_IMAGEN = 'imagen'
    TIPO_DATA_TEXTO = 'texto'
    TIPO_DATA_NUMERICO = 'numerico'

    OPCIONES_TIPO_DATA = (
        (TIPO_DATA_NUMERICO, 'Númerico'),
        (TIPO_DATA_TEXTO, 'Texto'),
        (TIPO_DATA_IMAGEN, 'Imagen'),
    )

    nombreDataSet = models.CharField(primary_key=True, max_length=30)
    tipoDataSet = models.CharField(max_length=40, verbose_name="Tipo datos", choices=OPCIONES_TIPO_DATA,
                                   default=TIPO_DATA_TEXTO)
    tamañoDataSet = models.IntegerField(max_length=40)
    datos = models.FileField(upload_to='Archivos/dataSet', null=True, blank=False)

    def __str__(self):
        return '{}'.format(self.nombreDataSet)




