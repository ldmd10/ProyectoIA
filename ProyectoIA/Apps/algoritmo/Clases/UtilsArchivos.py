import json
import csv


def leerDatos(ruta):
    with open(ruta) as file:
        datosInput = json.load(file)
    return datosInput
