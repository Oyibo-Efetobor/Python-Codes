import requests
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.getenv("sheet_endpoint_key")


exercise_headers = {
    "x-app-id": os.getenv("x_app_id"),
    "x-app-key": os.getenv("x_app_key"),
    "Content-Type": "application/json"
}

user_input = input("What was your exercise today and how long?: ")

exercise_parameters = {
    "query": user_input
}

exercise_response = requests.post(
    url=exercise_endpoint,
    json=exercise_parameters,
    headers=exercise_headers
)

exercise_response.raise_for_status()
exercise_data = exercise_response.json()

exercise = (exercise_data['exercises'][0]['user_input'])
duration = (exercise_data['exercises'][0]['duration_min'])
calories = (exercise_data['exercises'][0]['nf_calories'])

date = str(datetime.now().date())
time = str(datetime.now().time().strftime("%H:%M"))

post_exercise_parameters = {
    "sheet1":{
        "date":date,
        "time":time,
        "exercise":exercise,
        "duration":duration,
        "calories":calories
    }
}

post_exercise_headers ={
    "Authorization": os.getenv("bearer_auth")
}

post_exercise_response = requests.post(
    url=sheet_endpoint,
    json=post_exercise_parameters,
    headers=post_exercise_headers
)

post_exercise_response.raise_for_status()