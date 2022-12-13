import requests
from datetime import datetime
today = datetime.now()

USERNAME = "***"
TOKEN = "***"
GRAPH_ID = "graph1"
DATE = 20220603
TODAY = today.strftime('%Y%m%d')

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_id_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
graph_id_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"

pixela_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_params = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "pages",
    "type": "int",
    "color": "kuro"
}

graph_id_params = {
    "date": DATE,
    "quantity": "150"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_id_update_params = {
    "date": TODAY,
    "quantity": input("How many pages did you read today? ")
}
response = requests.put(url=graph_id_update_endpoint, json=graph_id_update_params, headers=headers)
print(response.text)


