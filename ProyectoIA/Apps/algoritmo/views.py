from django.shortcuts import render


# Create your views here.

def algotimos_list(request):
    return render(request, 'algoritmo/algoritmo_list.html', {})
