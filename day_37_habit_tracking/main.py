import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

USERNAME = "efetobordev"
TOKEN = os.getenv("token_code")
GRAPH_ID = "graph1"

#CREATE USER 
pixela_endpoint = "https://pixe.la/v1/users"

pixela_parameters= {
    "token": TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}



# pixela_response = requests.post(url=pixela_endpoint, json=pixela_parameters)
# print(pixela_response.text)

#CREATE GRAPH

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_parameters = {
    "id" : GRAPH_ID,
    "name": "My Running Graph",
    "unit" : "Km",
    "color" : "ajisai",
    "type" : "float"
}

ht_headers = {
    "X-USER-TOKEN" : TOKEN
}

# graph_response = requests.post(
#     url=graph_endpoint,
#     json=graph_parameters,
#     headers=ht_headers
#     )

today = (datetime.now()).strftime("%Y%m%d")

#CREATE PIXEL ON GRAPH

create_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

create_pixel_parameters = {
    "date":today,
    "quantity":"100.5",
    
}


# create_pixel_response = requests.post(
#     url = create_pixel_endpoint,
#     json = create_pixel_parameters,
#     headers=ht_headers
# )

# print(create_pixel_response.text)


#UPDATE PIXEL VALUE
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

update_pixel_parameters ={
    "quantity":"300"
}

# update_pixel_response = requests.put(
#     url = update_pixel_endpoint,
#     headers= ht_headers,
#     json=update_pixel_parameters
# )

# print(update_pixel_response.text)

#DELETE PIXEL VALUE

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

# delete_pixel_response = requests.delete(
#     url=delete_pixel_endpoint,
#     headers=ht_headers
# )

# print(delete_pixel_response.text)