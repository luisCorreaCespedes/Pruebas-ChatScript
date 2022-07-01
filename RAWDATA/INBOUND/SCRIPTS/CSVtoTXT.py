#Librerías
import csv
import os
import hashlib

def ejecucionScript():

    #Lectura de ficheros csv que hay en el directorio
    directorio = "../ARCHIVO_CARGA/"
    with os.scandir(directorio) as ficheros:
        ficheros = [fichero.name for fichero in ficheros if fichero.is_file() and fichero.name.endswith('.csv')]

    #Obtención de hash de cada csv para su comparación
    for elemento in ficheros:
        file = open("../ARCHIVO_CARGA/" + elemento, 'rb')
        h = hashlib.sha1()
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
        file.close()

        #Si no hay datos en el txt, se agrega el primer hash del csv correspondiente
        listadoHash = open("../ARCHIVO_CARGA/hash.txt", 'r+')
        if os.stat("../ARCHIVO_CARGA/hash.txt").st_size == 0:
            listadoHash.close()
            print('[LOG]: El archivo esta vacío. Se ha agregado el HASH ' + h.hexdigest())
            agregarDatos(elemento, h)

        #Si el hash no está en la lista, se agrega al final
        elif h.hexdigest() not in listadoHash.read():
            listadoHash.close()
            print('[LOG]: Se ha agregado el HASH ' + h.hexdigest())
            agregarDatos(elemento, h)
        
        #Si el hash está, no se hace nada
        else: print('[LOG]: El HASH ' + h.hexdigest() + ' ya está en la lista.')


def agregarDatos(ruta, h):

    #Se agrega el hash correspondiente al listado de hash
    agregarHash = open("../ARCHIVO_CARGA/hash.txt", 'a+')
    agregarHash.write(str(h.hexdigest()) + '\n')
    agregarHash.close()

    #Se leen los datos del csv
    entrada = open("../ARCHIVO_CARGA/" + ruta, encoding="utf-8")
    datos = csv.DictReader(entrada)
    nuevosDatos = list(datos)
    entrada.close()
    print('[LOG]: Se cargaron los datos del CSV.')

    #Se cargan los datos necesarios al txt correspondiente
    salida = open("../DATOS/datos.txt", "a", encoding="utf-8")
    resultados = csv.DictWriter(salida, fieldnames=['empresa', 'tipo', 'producto', 'nombre'], extrasaction='ignore', delimiter='\t', lineterminator='\n')
    resultados.writerows(nuevosDatos)
    salida.close()
    print('[LOG]: Se agregaron los datos al TXT.')