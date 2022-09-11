import requests
import json
import datetime

# On importe la liste des jours pou lesquels on a déjà les données
with open("days.txt", "r") as days:
    completed_days = days.read()
    days.close()
    
# On importe la date d'aujourd'hui et on la formatte
today = datetime.datetime.now()
today = str(today).split(" ")
today = today[0]

# On regarde si l'on a déjà les données d'aujourd'hui
if today not in completed_days:
    auth_key = input("Enter your own API key: ")
    # Si on a pas encore les données
    # On fait une requête à l'API Stormglass
    response = requests.get(
        "https://api.stormglass.io/v2/weather/point",
        params={
            # Villers-sur-Mer : 49.32195479823806, -0.011785196637717673
            "lat": 49.322,
            "lng": -0.012,
            "params": "windSpeed",
        },
        headers={
            "Authorization": auth_key
        }
    )

    # Copies results and formats them too
    json_data = response.json()
    filename = "wind_villers_"+str(datetime.datetime.now())[0:10]+".json"
    with open(filename, "w") as data:
        json.dump(json_data, data, indent=4)
        data.writelines("\n")
        data.close()
    with open("days.txt", "a") as days:
        days.writelines(today)
        days.writelines("\n")
        days.close()
