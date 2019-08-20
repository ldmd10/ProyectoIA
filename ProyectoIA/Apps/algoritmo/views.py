from django.shortcuts import render, redirect
from django.views.generic import ListView
from Apps.algoritmo.forms import FormConfAlgoritmoCluster
from Apps.algoritmo.forms import FormConfAlgoritmoApriori
from Apps.algoritmo.forms import FormConfAlgoritmoFpGrowth
from Apps.algoritmo.models import Entrenamiento
from Apps.algoritmo.models import AlgoritmoReglas
from Apps.dataSet.models import DataSet

from Apps.algoritmo.models import Algoritmo


# Create your views here.
class ListarAlgoritmos(ListView):
    model = Algoritmo
    template_name = 'algoritmo_list.html'


def viewConfEjecucion(request, pkAlgoritmo):
    algoritmo = Algoritmo.objects.get(id=pkAlgoritmo)
    if algoritmo.nombreAlgoritmo == "Kmeans":
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
                return render(request, 'conf_algoritmo.html',
                              {'form': form, 'algoritmo': algoritmo, 'entrenamiento': entrenamientoNuevo,
                               'apriori': None, 'fp': None})
        else:
            form = FormConfAlgoritmoCluster()
    if algoritmo.nombreAlgoritmo == "Apriori":
        if (request.method == 'POST'):
            form = FormConfAlgoritmoApriori(request.POST)
            foraneaDataSet = request.POST.get("foraneaDataSet")
            minSuport = request.POST.get("minSuport")
            minConfianza = request.POST.get("minConfianza")
            tamañoCondicion = request.POST.get("tamañoCondicion")
            tamañoPredicado = request.POST.get("tamañoPredicado")
            if form.is_valid():
                dataSetSeleccionado = DataSet.objects.get(idDataSet=foraneaDataSet)
                apriori = AlgoritmoReglas(minSuport=minSuport,
                                          foraneaDataSet=dataSetSeleccionado,
                                          foraneaAlgoritmo=algoritmo,
                                          minConfianza=minConfianza,
                                          tamañoCondicion=tamañoCondicion,
                                          tamañoPredicado=tamañoPredicado)
                apriori.save()
                return render(request, 'conf_algoritmo.html',
                              {'form': form, 'algoritmo': algoritmo, 'entrenamiento': None, 'apriori': apriori,
                               'fp': None})
        else:
            form = FormConfAlgoritmoApriori()
    if algoritmo.nombreAlgoritmo == "FpGrowth":
        if (request.method == 'POST'):
            form = FormConfAlgoritmoFpGrowth(request.POST)
            foraneaDataSet = request.POST.get("foraneaDataSet")
            minimoFrecuencia = request.POST.get("minimoFrecuencia")
            minConfianza = request.POST.get("minConfianza")
            if form.is_valid():
                dataSetSeleccionado = DataSet.objects.get(idDataSet=foraneaDataSet)
                fpGrowth = AlgoritmoReglas(minimoFrecuencia=minimoFrecuencia,
                                           foraneaDataSet=dataSetSeleccionado,
                                           foraneaAlgoritmo=algoritmo,
                                           minConfianza=minConfianza,
                                           )
                fpGrowth.save()
                return render(request, 'conf_algoritmo.html',
                              {'form': form, 'algoritmo': algoritmo, 'entrenamiento': None, 'apriori': None,
                               'fp': fpGrowth})
        else:
            form = FormConfAlgoritmoFpGrowth()

    return render(request, 'conf_algoritmo.html',
                  {'form': form, 'algoritmo': algoritmo, 'entrenamiento': None, 'apriori': None, 'fp': None})
