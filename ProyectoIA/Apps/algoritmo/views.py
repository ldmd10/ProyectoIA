from django.shortcuts import render, redirect
from django.views.generic import ListView
from Apps.algoritmo.forms import FormConfAlgoritmoCluster
from Apps.algoritmo.models import Entrenamiento
from Apps.dataSet.models import DataSet

from Apps.algoritmo.models import Algoritmo


# Create your views here.
class ListarAlgoritmos(ListView):
    model = Algoritmo
    template_name = 'algoritmo_list.html'


def viewConfEjecucion(request, pkAlgoritmo):
    algoritmo = Algoritmo.objects.get(id=pkAlgoritmo)
    if (request.method == 'POST'):
        form = FormConfAlgoritmoCluster(request.POST)
        tituloEntrenamiento = request.POST.get("tituloEntrenamiento")
        foraneaDataSet = request.POST.get("foraneaDataSet")
        k = request.POST.get("k")
        print("--------------------")
        print(k)
        print(tituloEntrenamiento)
        print(foraneaDataSet)
        if form.is_valid():
            dataSetSeleccionado = DataSet.objects.get(idDataSet=foraneaDataSet)
            entrenamientoNuevo = Entrenamiento(tituloEntrenamiento=tituloEntrenamiento,
                                               foraneaDataSet=dataSetSeleccionado,
                                               foraneaAlgoritmo=algoritmo, k=k)
            entrenamientoNuevo.save()
            return render(request, 'conf_alg_cluster.html',
                          {'form': form, 'algoritmo': algoritmo, 'entrenamiento': entrenamientoNuevo})

    else:
        form = FormConfAlgoritmoCluster()
    return render(request, 'conf_alg_cluster.html', {'form': form, 'algoritmo': algoritmo, 'entrenamiento': None})
