import pandas as pd
import os 
import time 
import pathlib
import csv
from datetime import datetime
from verify_utf8 import verify


def date_time (fichero):
    ti_m = os.path.getmtime(fichero) 
    m_ti = time.ctime(ti_m)
    t_obj = time.strptime(m_ti) 
  
    T_date = time.strftime("%Y-%m-%d", t_obj) 
    T_time = time.strftime("%H:%M:%S", t_obj)
    return  T_date, T_time

def mayor(time):
    aux = ''
    for hour in time:
        if (hour > aux): aux = hour
    return aux


def write_txt(text):
    f = open("date_carga.txt","w")
    f.write(text); f.close()

def zero(now_time):
    if(now_time == "00:00:00"): 
        f = open("date_carga.txt","w"); f.close()

def copy(fichero,_data):
    dataset = pd.read_csv(fichero,sep=';')
    dataset.to_csv(_data, sep=" ")
    verify(fichero)

def load_data(_directory, _data):
    #ruta donde se encuentra la carpeta de los archivos csv
    directory = pathlib.Path(_directory)

    #fecha y tiempo actual
    now = datetime.now(); now_date= now.date(); now_time = now.time().strftime("%H:%M:%S")
    zero(now_time)

    ficheros = []; time = []
  

    #hora y fecha de todos los archivos dentro de la carpeta
    for fichero in directory.iterdir():
        T_date, T_time = date_time(fichero)
        if(str(now_date) == T_date):
            ficheros.append(fichero)
            time.append(T_time)
    
    lst_m = mayor(time) #ultima modificacion

    if os.stat("date_carga.txt").st_size == 0:
        write_txt(lst_m)
        copy((ficheros[time.index(lst_m)]),_data)

    else: 
        f = open("date_carga.txt"); date_carga = f.readline()
        if(lst_m > date_carga):
            write_txt(lst_m)
            copy((ficheros[time.index(lst_m)]),_data)