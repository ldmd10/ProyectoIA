from django import forms
from Apps.algoritmo.models import Algoritmo


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
