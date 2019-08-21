import json
import csv


def leerDatos(ruta):
    with open(ruta) as file:
        print("cdmefd ve f \n" + ruta)
        datosInput = json.load(file)
    return datosInput


def leerCsv(ruta):
    salida = "\n"
    with open(ruta, newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            salida = salida + str(row) + "\n"
    return salida
