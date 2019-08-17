from django import forms
from Apps.dataSet.models import DataSet


class AgregarDataSet(forms.ModelForm):
    class Meta:
        model = DataSet
        fields = [
            'nombreDataSet',
            'tipoDataSet',
            'tamañoDataSet',
            'datos',
        ]
        labels = {
            'nombreDataSet': 'Nombre',
            'tipoDataSet': 'Tipo',
            'tamañoDataSet': 'Tamaño',
            'datos': 'Datos',

        }
        widgets = {
            'nombreDataSet': forms.TextInput(attrs={'class': 'form-control'}),
            'tipoDataSet': forms.TextInput(attrs={'class': 'form-control'}),
            'tamañoDataSet': forms.NumberInput(attrs={'class': 'form-control'}),
            'datos': forms.ClearableFileInput(),

        }
