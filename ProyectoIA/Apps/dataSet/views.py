from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from Apps.dataSet.models import DataSet
from Apps.dataSet.forms import AgregarDataSet

# Create your views here.
class ListarData(ListView):
    model = DataSet
    template_name='list_data_set.html'


class AgregarData(CreateView):
    model=DataSet
    from_class= AgregarDataSet
    template_name = 'agregar_data_set.html'

    def get_success_url(self):
        return reverse('course:ListarData')

