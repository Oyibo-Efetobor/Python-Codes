#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager


from datetime import datetime, timedelta
from dotenv import load_dotenv
load_dotenv()

data_manager = DataManager()

#get iata codes and send to sheet
data_manager.send_iata_to_sheet()
#send cheapest flight to sheet
data_manager.send_cheapest_flight_to_sheet()

#send sms
#########################PENDING DUE TO API PRICE###################

