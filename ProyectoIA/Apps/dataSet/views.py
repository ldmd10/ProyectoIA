from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from Apps.dataSet.models import DataSet
from Apps.dataSet.forms import AgregarDataSet
from django.utils import timezone
from django.views.generic.detail import DetailView


# Create your views here.
class ListarData(ListView):
    model = DataSet
    template_name = 'list_data_set.html'


class DataSetDetalle(DetailView):
    model = DataSet
    template_name = 'dataset_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


def vewAgregarDataSet(request):
    if (request.method == 'POST'):
        form = AgregarDataSet(request.POST)
        files = request.FILES.getlist('datos')
        nombreDataSet = request.POST.get("nombreDataSet")
        tipoDataSet = request.POST.get("tipoDataSet")
        tamañoDataSet = request.POST.get("tamañoDataSet")
        claseData = request.POST.get("claseDataSet")
        if form.is_valid():
            dataSetNuevo = DataSet(
                nombreDataSet=nombreDataSet,
                tipoDataSet=tipoDataSet,
                tamañoDataSet=tamañoDataSet)
            dataSetNuevo.save()
            if tipoDataSet == "imagen":
                for f in files:
                    dataSetNuevo.imagendata_set.create(clase=claseData, imagen=f)
            else:
                dataSetNuevo.datos = files.__getitem__(0)
            dataSetNuevo.save()
            print(dataSetNuevo.imagendata_set.count())

            # form.save()

            return redirect('ListarData')
    else:
        form = AgregarDataSet()
    return render(request, 'agregar_data_set.html', {'form': form})
