#Importación archivo .csv para lectura
import csv
entrada = open("../ARCHIVO_CARGA/Base-Cocacola-17-06-2022.csv")
datos = csv.reader(entrada)

#Exportación archivo .txt con datos del .csv
salida = open("../DATOS/datos.txt", "w")
for fila in datos:
    for columna in fila:
        salida.write(columna)
        salida.write("\t")
    salida.write("\n")
    

salida.close()
entrada.close()
