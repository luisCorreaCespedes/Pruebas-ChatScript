import CSVtoTXT
import time

def timerScript():
    CSVtoTXT.ejecucionScript()
    time.sleep(10)  #CAMBIAR POR 60 SEGUNDOS

while True:
    timerScript()
