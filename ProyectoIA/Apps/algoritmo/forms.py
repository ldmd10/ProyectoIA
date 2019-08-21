from django import forms
from Apps.algoritmo.models import Algoritmo
from Apps.algoritmo.models import Entrenamiento
from Apps.algoritmo.models import AlgoritmoReglas
from Apps.algoritmo.models import Id3


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


class FormConfAlgoritmoApriori(forms.ModelForm):
    class Meta:
        model = AlgoritmoReglas
        fields = [
            "foraneaDataSet",
            "minConfianza",
            "minSuport",
            "tamañoCondicion",
            "tamañoPredicado",

        ]
        labels = {
            'foraneaDataSet': 'Seleccione dataSet',
            'minConfianza': 'Confianza minima ',
            "minSuport": "Soporte minimo",
            "tamañoCondicion": "Tamaño condición",
            "tamañoPredicado": "Tamaño predicado",

        }
        widgets = {
            'foraneaDataSet': forms.Select(attrs={'class': 'form-control mdb-select colorful-select dropdown-ins'}),
            'minConfianza': forms.NumberInput(attrs={'class': 'form-control'}),
            'minSuport': forms.NumberInput(attrs={'class': 'form-control'}),
            "tamañoCondicion": forms.NumberInput(attrs={'class': 'form-control'}),
            "tamañoPredicado": forms.NumberInput(attrs={'class': 'form-control'}),
        }


class FormConfAlgoritmoFpGrowth(forms.ModelForm):
    class Meta:
        model = AlgoritmoReglas
        fields = [
            "foraneaDataSet",
            "minConfianza",
            "minimoFrecuencia",

        ]
        labels = {
            'foraneaDataSet': 'Seleccione dataSet',
            'minConfianza': 'Confianza minima ',
            "minimoFrecuencia": "Minimo de frecuencia",

        }
        widgets = {
            'foraneaDataSet': forms.Select(attrs={'class': 'form-control mdb-select colorful-select dropdown-ins'}),
            'minConfianza': forms.NumberInput(attrs={'class': 'form-control'}),
            "minimoFrecuencia": forms.NumberInput(attrs={'class': 'form-control'}),
        }


class FormConfAlgoritmoId3(forms.ModelForm):
    class Meta:
        model = Id3
        fields = [
            "foraneaDataSet",
            "entradaPrueba",

        ]
        labels = {
            'foraneaDataSet': 'Seleccione dataSet',
            'entradaPrueba': 'Test',

        }
        widgets = {
            'foraneaDataSet': forms.Select(attrs={'class': 'form-control mdb-select colorful-select dropdown-ins'}),
            'entradaPrueba': forms.Select(attrs={'class': 'form-control mdb-select colorful-select dropdown-ins'}),
        }


'''class FormTestAlgoritmoId3(forms.ModelForm):
    class Meta:
        model = TestId3
        fields = [
            "tituloTest",
            "textoPrueba",
            "datoPrueba",

        ]
        labels = {
            "tituloTest": "Titulo test",
            "textoPrueba": "Entrada manual",
            "datoPrueba": "Entrada Archivo",

        }
        widgets = {
            'tituloTest': forms.Select(attrs={'class': 'form-control mdb-select colorful-select dropdown-ins'}),
            "textoPrueba": forms.Textarea(attrs={'class': 'form-control'}),
            'datoPrueba': forms.ClearableFileInput(),
        }
'''
