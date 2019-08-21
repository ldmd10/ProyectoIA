# Generated by Django 2.2.3 on 2019-08-19 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('idDataSet', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('nombreDataSet', models.CharField(max_length=30)),
                ('tipoDataSet', models.CharField(choices=[('numerico', 'Númerico'), ('texto', 'Texto'), ('imagen', 'Imagen')], default='texto', max_length=40, verbose_name='Tipo datos')),
                ('tamañoDataSet', models.IntegerField()),
                ('datos', models.FileField(blank=True, null=True, upload_to='Archivos/dataSet')),
            ],
        ),
        migrations.CreateModel(
            name='ImagenData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clase', models.CharField(max_length=50)),
                ('imagen', models.FileField(null=True, upload_to='Archivos/dataSet')),
                ('dataSet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataSet.DataSet')),
            ],
        ),
    ]