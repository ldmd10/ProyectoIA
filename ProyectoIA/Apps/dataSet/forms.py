from django import forms
from Apps.dataSet.models import DataSet


class AgregarDataSet(forms.ModelForm):
    class Meta:
        model = DataSet
        fields = [
            'nombreDataSet',
            'tipoDataSet',
            'tamañoDataSet',
            # 'datos',
        ]
        labels = {
            'nombreDataSet': 'Nombre',
            'tipoDataSet': 'Tipo',
            'tamañoDataSet': 'Tamaño',
            # 'datos': 'Datos',
        }
        widgets = {
            'nombreDataSet': forms.TextInput(attrs={'class': 'form-control'}),
            'tipoDataSet': forms.Select(attrs={'class': 'form-control mdb-select colorful-select dropdown-ins'}),
            # forms.TextInput(attrs={'class': 'form-control'}),
            'tamañoDataSet': forms.NumberInput(attrs={'class': 'form-control'}),
            # 'datos': forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True})),

        }
