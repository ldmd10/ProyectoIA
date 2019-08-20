from django.urls import path
from . import views
from Apps.algoritmo.views import ListarAlgoritmos
from Apps.algoritmo.views import viewConfEjecucion
from django.conf.urls import url

urlpatterns = [
    url(r'^algoritmos/', ListarAlgoritmos.as_view(), name='ListarAlgoritmos'),
    url(r'^ejecucion/(?P<pkAlgoritmo>\d+)/conf', viewConfEjecucion, name='ejecucionConf'),
]
