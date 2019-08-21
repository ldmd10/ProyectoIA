from Apps.algoritmo.Clases.id3.ID3_C import ID3_C
import numpy as np

datos = np.genfromtxt('C:/Users/LuisDavid102/Desktop/futbol.csv', delimiter=',', dtype="str")
x = datos[:, :-1]  # obtengo los valores de la entrada de datos de cada individuo
y = datos[:, -1]  # obtengo las etiquetas de la entrada de datos para cada individuo

arbol = ID3_C()
arbol.entrenar(x, y)
# print(x)
print("-------------")
# print(y)
print()
salida = arbol.predecir(np.array([['graduado_escolar', 'alta', 'si', 'si'], ['graduado_escolar', 'alta', 'si', 'si'],
                                  ['graduado_escolar', 'alta', 'si', 'si'], ['graduado_escolar', 'alta', 'si', 'si'],
                                  ['graduado_escolar', 'alta', 'si', 'si'], ['graduado_escolar', 'alta', 'si', 'si']]))
print(salida)

# print('porcentaje de aciertos: ', 100 * sum(y == salida) / x.shape[0])
