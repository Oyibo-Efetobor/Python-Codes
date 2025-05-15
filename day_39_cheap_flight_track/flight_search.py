import requests
import os
# Load environment variables
from dotenv import load_dotenv
load_dotenv()

class FlightSearch:
    def __init__(self):   

    # API credentials
        self.api_key = os.getenv("flight_api_key")
        self.api_secret = os.getenv("flight_api_secret")

    # Step 1: Get the access token
    def get_iata_code(self, user_input):
        security_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        security_headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        security_parameters = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }

        # Make the POST request to get the token
        security_response = requests.post(
            url=security_url,
            headers=security_headers,
            data=security_parameters
        )
        security_response.raise_for_status()  # Raise an error if the request fails
        security_data = security_response.json()
        bearer_token = security_data["access_token"]

        iata_url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        
        iata_headers = {
            "Authorization" : f"Bearer {bearer_token}"
        }
        
        
        iata_parameters ={
            "keyword":user_input
        }
        
        iata_response = requests.get(
            url=iata_url,
            params=iata_parameters,
            headers=iata_headers
        )
        
        iata_response.raise_for_status()
        iata_data = iata_response.json()
        return str(iata_data["data"][0]["iataCode"])

