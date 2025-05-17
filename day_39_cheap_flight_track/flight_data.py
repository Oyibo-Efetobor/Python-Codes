from datetime import datetime, timedelta
import requests
import os
# Load environment variables
from dotenv import load_dotenv
load_dotenv()

class FlightData:
    def __init__(self):   

    # API credentials
        self.api_key = os.getenv("flight_api_key")
        self.api_secret = os.getenv("flight_api_secret")

    def get_cheapest_flight(self, origin_iata, destination_iata):
        # Get access token
        security_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        security_headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        security_parameters = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }
        security_response = requests.post(
            url=security_url,
            headers=security_headers,
            data=security_parameters
        )
        security_response.raise_for_status()
        security_data = security_response.json()
        bearer_token = security_data["access_token"]

        # Set search dates
        tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        six_months_later = (datetime.now() + timedelta(days=180)).strftime("%Y-%m-%d")

        # Search for cheapest flight
        search_url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        search_headers = {
            "Authorization": f"Bearer {bearer_token}"
        }
        search_params = {
            "originLocationCode": origin_iata,
            "destinationLocationCode": destination_iata,
            "departureDate": tomorrow,
            "returnDate": six_months_later,
            "adults": 1,
            "currencyCode": "USD",
            "max": 1  # Get only the cheapest
        }
        response = requests.get(
            url=search_url,
            headers=search_headers,
            params=search_params
        )
        response.raise_for_status()
        data = response.json()
        # Extract the cheapest price if available
        if "data" in data and data["data"]:
            price = data["data"][0]["price"]["total"]
            return price
        else:
            return None
flight_data = FlightData()

print(flight_data.get_cheapest_flight("YBR","PAR")) #brandon