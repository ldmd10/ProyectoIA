from django.urls import path
from django.conf.urls import url
from Apps.dataSet.views import ListarData
from Apps.dataSet.views import vewAgregarDataSet
from Apps.dataSet.views import DataSetDetalle

from . import views

urlpatterns = [
    url(r'^datasets/', ListarData.as_view(), name='ListarData'),
    url(r'^agregardataset/', vewAgregarDataSet, name='AgregarData'),
    url(r'^data/(?P<pk>\d+)$', DataSetDetalle.as_view(), name='dataset_detalle'),

]
