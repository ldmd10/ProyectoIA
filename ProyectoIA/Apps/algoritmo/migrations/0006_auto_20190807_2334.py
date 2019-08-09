# Generated by Django 2.2.3 on 2019-08-08 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('algoritmo', '0005_auto_20190807_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='ejecucion',
            name='foraneaEntrenamiento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='algoritmo.Entrenamiento'),
        ),
        migrations.AlterField(
            model_name='ejecucion',
            name='foraneaAlgoritmo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='algoritmo.Algoritmo'),
        ),
    ]