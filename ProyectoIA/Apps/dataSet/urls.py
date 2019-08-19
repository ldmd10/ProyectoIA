from django.urls import path
from django.conf.urls import url
from Apps.dataSet.views import ListarData
from Apps.dataSet.views import AgregarData
from Apps.dataSet.views import vewAgregarDataSet

from . import views

urlpatterns = [
    url(r'^datasets/', ListarData.as_view(), name='ListarData'),
    url(r'^agregardataset/', vewAgregarDataSet, name='AgregarData'),

]
