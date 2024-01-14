import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
MY_TOKEN = os.getenv("PIXELA_TOKEN")
pixela_url = "https://pixe.la/v1/users"
USERNAME = "djay"

params = {
    "token": "MY_TOKEN",
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# create user
# response = requests.post(url=pixela_url, json=params)
#
# print(response.text)

graph_endpoint = f"{pixela_url}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Study Graph",
    "unit": "hour",
    "type": "float",
    "color": "sora"
}

# create graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers={"X-USER-TOKEN": MY_TOKEN})
#
# print(response.text)

# create pixel
pixel_endpoint = f"{pixela_url}/{USERNAME}/graphs/graph1"

today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1.00",
}

# post pixel
# response = requests.post(url=pixel_endpoint, json=pixel_config, headers={"X-USER-TOKEN": MY_TOKEN})

# print(response.text)

# update pixel
pixela_update_endpoint = f"{pixela_url}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"

pixela_update_config = {
    "quantity": "2.00",
}

# pixel_update_response = requests.put(url=pixela_update_endpoint, json=pixela_update_config, headers={"X-USER-TOKEN": MY_TOKEN})
# print(pixel_update_response.text)

# Delete pixel

delete_endpoint = f"{pixela_url}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
# pixel_delete_response = requests.delete(url=pixela_update_endpoint, headers={"X-USER-TOKEN": MY_TOKEN})
# print(pixel_delete_response.text)


