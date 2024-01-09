import os
import requests
from dotenv import load_dotenv

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
response = requests.post(url=graph_endpoint, json=graph_config, headers={"X-USER-TOKEN": MY_TOKEN})

print(response.text)