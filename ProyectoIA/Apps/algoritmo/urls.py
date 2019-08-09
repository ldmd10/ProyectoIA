from django.urls import path
from . import views

urlpatterns = [
    path('', views.algotimos_list, name='algoritmos_list'),

]
