from django.urls import path
from . import views
from Apps.algoritmo.views import ListarAlgoritmos
from django.conf.urls import url

urlpatterns = [
    url(r'^algoritmos/', ListarAlgoritmos.as_view(), name='ListarAlgoritmos'),

]
