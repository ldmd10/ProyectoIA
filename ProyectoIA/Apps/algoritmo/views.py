from django.shortcuts import render
from django.views.generic import ListView

from Apps.algoritmo.models import Algoritmo
from Apps.dataSet.models import DataSet


# Create your views here.
class ListarAlgoritmos(ListView):
    model = Algoritmo
    template_name = 'list_algoritmos.html'
