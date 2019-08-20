import json


def leerDatos(ruta):
    with open(ruta) as file:
        print("cdmefd ve f \n" + ruta)
        datosInput = json.load(file)
    return datosInput
