# Generated by Django 2.2.3 on 2019-08-19 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dataSet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Algoritmo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreAlgoritmo', models.CharField(max_length=200, null=True, verbose_name='Nombre algoritmo')),
                ('tipo', models.CharField(choices=[('supervisado', 'Supervisado'), ('no supervisado', 'No supervisado')], default='no supervisado', max_length=100)),
                ('descripcion', models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Entrenamiento',
            fields=[
                ('idEntrenamiento', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('tituloEntrenamiento', models.CharField(max_length=80, verbose_name='Titulo entrenamiento')),
                ('tiempoEntrenamiento', models.DurationField(null=True, verbose_name='Tiempo entrenamiento')),
                ('foraneaAlgoritmo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='algoritmo.Algoritmo', verbose_name='Algoritmo')),
                ('foraneaDataSet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dataSet.DataSet', verbose_name='DataSet')),
            ],
        ),
        migrations.CreateModel(
            name='Ejecucion',
            fields=[
                ('idEjecucion', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('tituloEjecucion', models.CharField(max_length=80)),
                ('datoPrueba', models.FileField(null=True, upload_to='Archivos/Prueba')),
                ('tiempoEjecucion', models.TimeField()),
                ('foraneaAlgoritmo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='algoritmo.Algoritmo')),
                ('foraneaEntrenamiento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='algoritmo.Entrenamiento')),
            ],
        ),
    ]
