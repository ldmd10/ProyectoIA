from django import forms
from Apps.algoritmo.models import Algoritmo
from Apps.algoritmo.models import Entrenamiento


class FormListAlgoritmo(forms.ModelForm):
    class Meta:
        model = Algoritmo
        fields = [
            'nombreAlgoritmo',
            'tipo',
            'descripcion',
        ]
        labels = {
            'nombreAlgotimo': 'Nombre',
            'tipo': 'Tipo',
            'descripcion': 'descripcion',
        }
        widgets = {
            'nombreAlgoritmo': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }


class FormConfAlgoritmoCluster(forms.ModelForm):
    class Meta:
        model = Entrenamiento
        fields = [
            'tituloEntrenamiento',
            'foraneaDataSet',
            'k',
        ]
        labels = {
            'tituloEntrenamiento': 'Titulo entrenamiento',
            'foraneaDataSet': 'Seleccione dataSet',
            'k': 'Ingrese k '
        }
        widgets = {
            'tituloEntrenamiento': forms.TextInput(attrs={'class': 'form-control'}),
            'foraneaDataSet': forms.Select(attrs={'class': 'form-control mdb-select colorful-select dropdown-ins'}),
            'k': forms.NumberInput(attrs={'class': 'form-control'})
        }
