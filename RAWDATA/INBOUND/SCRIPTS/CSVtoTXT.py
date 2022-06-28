#Librerías
import csv
import os

def ejecucionScript():

    #Carga de ficheros
    directorio = "../ARCHIVO_CARGA/"
    with os.scandir(directorio) as ficheros:
        ficheros = [fichero.name for fichero in ficheros if fichero.is_file() and fichero.name.endswith('.csv')]

    #Lectura de ficheros
    for rutas in ficheros:
        entrada = open("../ARCHIVO_CARGA/" + rutas, encoding="utf-8")
        datos = csv.DictReader(entrada)
        lista = list(datos)

        #Exportación fichero .txt con datos del .csv
        salida = open("../DATOS/datos.txt", "a", encoding="utf-8")
        resultados = csv.DictWriter(salida, fieldnames=['empresa', 'tipo', 'producto', 'nombre'], extrasaction='ignore', delimiter='\t', lineterminator='\n')
        resultados.writerows(lista)

    salida.close()
    entrada.close()