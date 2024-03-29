# Generated by Django 2.2.3 on 2019-08-21 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataSet', '0002_auto_20190820_2319'),
        ('algoritmo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlgoritmoReglas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minSuport', models.FloatField(null=True)),
                ('minConfianza', models.FloatField(null=True)),
                ('tamañoCondicion', models.IntegerField(null=True)),
                ('tamañoPredicado', models.IntegerField(null=True)),
                ('minimoFrecuencia', models.IntegerField(null=True)),
                ('tiempoEntrenamiento', models.DurationField(null=True, verbose_name='Tiempo entrenamiento')),
                ('foraneaAlgoritmo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='algoritmo.Algoritmo', verbose_name='Algoritmo')),
                ('foraneaDataSet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dataSet.DataSet', verbose_name='DataSet')),
            ],
        ),
        migrations.CreateModel(
            name='DatosPrueba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clase', models.CharField(max_length=50)),
                ('tituloDataTest', models.CharField(max_length=50)),
                ('dato', models.FileField(null=True, upload_to='Archivos/Prueba')),
            ],
        ),
        migrations.CreateModel(
            name='Id3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempoEntrenamiento', models.DurationField(null=True, verbose_name='Tiempo entrenamiento')),
                ('tiempoEjecucion', models.TimeField(null=True)),
                ('entradaPrueba', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='algoritmo.DatosPrueba', verbose_name='Datos prueba')),
                ('foraneaAlgoritmo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='algoritmo.Algoritmo')),
                ('foraneaDataSet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dataSet.DataSet', verbose_name='DataSet')),
            ],
        ),
        migrations.AddField(
            model_name='entrenamiento',
            name='k',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Ejecucion',
        ),
    ]
