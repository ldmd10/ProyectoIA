from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from Apps.dataSet.models import DataSet
from Apps.dataSet.forms import AgregarDataSet


# Create your views here.
class ListarData(ListView):
    model = DataSet
    template_name = 'list_data_set.html'


class AgregarData(CreateView):
    # model = DataSet
    form_class = AgregarDataSet
    template_name = 'agregar_data_set.html'
    success_url = 'AgregarArchivo'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('datos')
        nombreDataSet = request.POST.get("nombreDataSet")
        tipoDataSet = request.POST.get("tipoDataSet")
        tamañoDataSet = request.POST.get("tamañoDataSet")

        if form.is_valid():
            print(DataSet.objects.all().count())
            for f in files:
                print()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


def vewAgregarDataSet(request):
    if (request.method == 'POST'):
        form = AgregarDataSet(request.POST)
        files = request.FILES.getlist('datos')
        nombreDataSet = request.POST.get("nombreDataSet")
        tipoDataSet = request.POST.get("tipoDataSet")
        tamañoDataSet = request.POST.get("tamañoDataSet")
        if form.is_valid():
            dataSetNuevo = DataSet(
                nombreDataSet=nombreDataSet,
                tipoDataSet=tipoDataSet,
                tamañoDataSet=tamañoDataSet)
            dataSetNuevo.save()

            if tipoDataSet == "imagen":
                for f in files:
                    dataSetNuevo.imagendata_set. \
                        create(clase="Carro", imagen=f)
            else:
                dataSetNuevo.datos = files.__getitem__(0)
            dataSetNuevo.save()
            print(dataSetNuevo.imagendata_set.count())

            # form.save()

            return redirect('index')
    else:
        form = AgregarDataSet()
    return render(request, 'agregar_data_set.html', {'form': form})
