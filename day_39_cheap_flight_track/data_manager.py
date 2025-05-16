# class DataManager:
#     #This class is responsible for talking to the Google Sheet.
#     pass
from flight_search import FlightSearch
import requests

flight_search = FlightSearch()

url = "https://api.sheety.co/8144b8d9ce6bc8d13cfe675fa3483490/flightDeals/sheet1"
row_count = 2
put_url = f"{url}/"

# Make the GET request
response = requests.get(url)
response.raise_for_status()  # Raise an error if the request fails

# Parse the JSON response
data = response.json()

# extract data
excel_dict = (data["sheet1"])

for i in range(len(excel_dict)):
    body = {
        "sheet1":{
            "city" : excel_dict[i]["city"],
            "iataCode": flight_search.get_iata_code(excel_dict[i]["city"])
        }
    }
    
    put_response = requests.put(
    url=put_url+f"{excel_dict[i]["id"]}",
    json=body
    )
    
    put_response.raise_for_status()