import json
import random
import math


def mostrarGrupos(cadena, k):
    print("k igual ", k)
    data = []
    for i in range(k):
        data.append([])
    for j in range(len(cadena)):
        data[cadena[j][1]].append(cadena[j][0])
    salida = ""
    for h in range(len(data)):
        salida = salida + "grupo " + str(h) + str(data[h]) + '\n'

    return (salida)


def kmeans(entrada, k):
    datoHistorico = ''
    dato = []
    datosEntrada = entrada
    centroide = []
    variable = int(k)
    for i in range(variable):
        centroide.append([])
        aleatorio = None
        for f in entrada:
            if (aleatorio == None):
                aleatorio = round(random.uniform(0, len(entrada[f]) - 1))  # centroides aleatorios se escogen
            centroide[i].append(entrada[f][aleatorio])
    for f in entrada:
        dato.append(entrada[f])
    # print(centroide)
    # print(dato[0], "atributo X1 ", dato[1], "atributo x2")
    datoHistorico = datoHistorico + "\n" + str(centroide) + "\n" + str(dato[0]) + " " + str(dato[1])
    resultadoCadena = None
    cambio = True
    while (cambio):
        cambio = False
        cadenaTemporal = []
        for i in range(len(dato[0])):
            lista = []
            for j in range(len(dato)):
                lista.append(dato[j][i])
            datoHistorico = datoHistorico + "\n" + str(lista) + " - individuo " + str(i)
            # print(lista, "individuo", i)
            cadenaTemporal.append(crearGrupo(lista, centroide, i))
        datoHistorico = datoHistorico + "\n" + str(cadenaTemporal)
        # print(cadenaTemporal)
        if resultadoCadena == None or not cadenasIguales(cadenaTemporal, resultadoCadena):
            resultadoCadena = cadenaTemporal
            for i in range(len(centroide)):
                for j in range(len(centroide[i])):
                    prom = 0;
                    con = 0
                    for k in range(len(resultadoCadena)):
                        if i == resultadoCadena[k][1]:
                            prom = prom + dato[j][resultadoCadena[k][0]]
                            con = con + 1
                    if con != 0:
                        prom = prom / con
                        centroide[i][j] = prom
            cambio = True
        datoHistorico = datoHistorico + "\n" + str(centroide) + " - centroides"
        # print(centroide, "centroides")
    global salidaGrupos
    salidaGrupos = mostrarGrupos(cadenaTemporal, variable)
    print(salidaGrupos)
    return datoHistorico, salidaGrupos


def crearGrupo(lista, centroide, item):
    mejorDistancia = None
    posicion = None
    for i in range(len(centroide)):
        Euclidia = 0
        for j in range(len(centroide[i])):
            Euclidia = Euclidia + pow(centroide[i][j] - lista[j], 2)
        Euclidia = math.sqrt(Euclidia)
        if mejorDistancia == None or Euclidia < mejorDistancia:
            mejorDistancia = Euclidia
            posicion = i
    return [item, posicion, mejorDistancia]


def cadenasIguales(cadenaTemporal, resultadoCadena):
    bandera = True
    if len(resultadoCadena) == len(cadenaTemporal):
        for i in range(len(resultadoCadena)):
            if resultadoCadena[i][1] != cadenaTemporal[i][1]:
                bandera = False
    return bandera


datosInput = {}


# print(datosInput)

def leerDatos(ruta):
    with open(ruta) as file:
        datosInput = json.load(file)
    return datosInput


datosEntrada = {
    "grupoA": [1.0, 1.5, 3.0, 5.0, 3.5, 4.5, 3.5],
    "grupoB": [1.0, 2.0, 4.0, 7.0, 5.0, 5.0, 4.5]
}
# algoritmo = K_means(datosEntrada, 3)
p, oellave = kmeans(datosEntrada, 3)

print(p)
print("------------")
print(oellave)
