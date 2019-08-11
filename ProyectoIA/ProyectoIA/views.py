from django.shortcuts import render
from django.http import HttpResponse
from Apps.algoritmo.models import Algoritmo
from Apps.dataSet.models import DataSet


'''def index(request):
    return render(request, template_name='index.html', context={"oe", "oemeraloca"})'''


def index(request):
    return render(request, "index.html")
