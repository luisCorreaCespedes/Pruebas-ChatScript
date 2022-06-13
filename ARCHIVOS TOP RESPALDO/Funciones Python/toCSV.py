import pandas as pd
import json

def _jsontocsv():
    data ='''
    {
    "Resultados":
            [
            { "Nombre": "JUAN", "Correo": "JUAN.1990@gmail.com", "resp1": "2", "resp2": "3", "resp3": "4", "resp4": "10" },
            { "Nombre": "CARLOS", "Correo": "CARLOS.1990@gmail.com", "resp1": "6", "resp2": "7", "resp3": "7", "resp4": "8" }
            ]
    }
    '''
    info = json.loads(data)

    df = pd.json_normalize(info['Resultados'])

    df.to_csv("samplecsv.csv")

'''_jsontocsv()'''