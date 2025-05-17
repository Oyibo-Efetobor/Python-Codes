from flight_search import FlightSearch
from flight_data import FlightData
import requests
import os 

class DataManager:
    def __init__(self):   

    # API credentials
        self.api_key = os.getenv("flight_api_key")
        self.api_secret = os.getenv("flight_api_secret")
        
        self.flight_search = FlightSearch()
        self.flight_data = FlightData()
        
        self.url = os.getenv("sheet_endpoint_key")
        self.put_url = f"{self.url}/"
        
        # Make the GET request
        self.response = requests.get(self.url)
        self.response.raise_for_status()  # Raise an error if the request fails

        # Parse the JSON response
        self.data = self.response.json()
        self.excel_dict = (self.data["sheet1"])
        
        self.sheety_headers = {
            "Authorization": os.getenv("bearer_auth")
        }

        
    def send_iata_to_sheet(self):
        

        for i in range(len(self.excel_dict)):
            body = {
                "sheet1":{
                    "city" : self.excel_dict[i]["city"],
                    "iataCode": self.flight_search.get_iata_code(self.excel_dict[i]["city"])
                }
            }
            
            put_response = requests.put(
            url=self.put_url+f"{self.excel_dict[i]["id"]}",
            json=body,
            headers=self.sheety_headers
            )
            
            put_response.raise_for_status()
        
    def from_location(self):
        response = requests.get(
            self.url,
            headers=self.sheety_headers
            )
        response.raise_for_status()
        data = response.json()
        
        location = str(data["sheet1"][0]["from"])
        from_location = str(self.flight_search.get_iata_code(location))
        return from_location
    
    def send_cheapest_flight_to_sheet(self):
        from_location = self.from_location()  # Only call once!
        for row in self.excel_dict:
            to_location = str(self.flight_search.get_iata_code(row["city"]))
            try:
                lowest_price = self.flight_data.get_cheapest_flight(from_location, to_location)
            except Exception as e:
                print(f"Error fetching price for {row['city']}: {e}")
                lowest_price = None

            body = {
                "sheet1": {
                    "city": row["city"],
                    "lowestPrice": lowest_price
                }
            }
            put_response = requests.put(
                url=self.put_url + f"{row['id']}",
                json=body,
                headers=self.sheety_headers
            )
            put_response.raise_for_status()
            
            
                  
# data_manager = DataManager()

# data_manager.send_cheapest_flight_to_sheet()