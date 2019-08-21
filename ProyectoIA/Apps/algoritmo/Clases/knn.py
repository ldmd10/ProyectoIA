import math
import numpy
from scipy.spatial import distance


def knn(json, k):
    listaDistancias = []
    listaIndices = []
    listaClases = {}

    for n in range(len(json["clases"])):
        listaClases[json["clases"][n]] = 0
        listaIndividuo = []
        i = 1
        while i <= (len(json) - 2):
            listaIndividuo.append(json[str(i)][n])
            i = i + 1
        distancia = distance.euclidean(listaIndividuo, json["target"])
        listaIndices.append([distancia, n])
        listaDistancias.append(distancia)

    listaDistancias.sort()
    salida1 = "\n"

    for i in range(k):
        for j in range(len(listaIndices)):
            if listaIndices[j][0] == listaDistancias[i]:
                salida1 = salida1 + str(listaIndices[j][1]) + " distancia " + str(
                    listaDistancias[i]) + " -- " + str(json["clases"][listaIndices[j][1]]) + "\n"
                listaClases[(json["clases"][listaIndices[j][1]])] = listaClases[
                                                                        (json["clases"][listaIndices[j][1]])] + 1
    mayor = 0
    keymayor = ""
    salidaRetorno = "\nEntrada de Datos :\n " + str(json)
    for key in listaClases.keys():
        if listaClases[key] > mayor:
            keymayor = key
            mayor = listaClases[key]

    salidaRetorno = salidaRetorno + "\n" + salida1 + "\n" + "-------------------------------" + "\n" + "Predición es " + keymayor
    return salidaRetorno


json = {
    "clases": ["rojo", "rojo", "naranja", "rojo", "rojo", "azul", "azul", "naranja", "azul", "naranja"],
    "target": [1, 3, 7],
    "1": [-1, -1, 0, 0, 1, 1, 1, 2, 4, 4],
    "2": [0, 1, 0, 1, 1, 2, 2, 3, 0, 0],
    "3": [2, 3, 1, 1, 1, 1, 5, 1, 0, 1],

}

# knn(json, 3)
