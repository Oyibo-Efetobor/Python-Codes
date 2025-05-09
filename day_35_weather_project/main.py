import os
from dotenv import load_dotenv

load_dotenv()

import requests


end_point = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": 8.140670,
    "lon": 5.102050,  # Landmark Uni
    "appid": os.getenv("weather_api_key"),
    "cnt":4,
}

response = requests.get(
    end_point,
    params=parameters
)

response.raise_for_status()
weather_data = response.json()

id_number = 0
weather_id_list = []

bring_umbrella = False

for i in range(4):
    weather_id_list.append(weather_data['list'][i]['weather'][0]['id'])
    if weather_data['list'][i]['weather'][0]['id'] < 700:
        bring_umbrella = True
        break

if bring_umbrella:
    print("Bring ☔")
else:
    print("Don't bring ☔")

