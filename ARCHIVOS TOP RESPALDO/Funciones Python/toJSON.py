import pandas as pd
import json

def _jsontoBot():
    csv_data = pd.read_csv("datos.txt", sep = ",")

    result = csv_data.to_json(orient="records")

    parsed = json.loads(result)

    tochatscritp = json.dumps(parsed[0], indent=4)

    print(tochatscritp)

'''_jsontoBot'''