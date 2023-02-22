import requests
import os

API_ENDPOINT = os.environ.get("SHEETY_API_ENDPOINT")

headers = {
    "Content-Type": "application/json",
}


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_cities_data(self):
        response = requests.get(
            url=API_ENDPOINT, headers=headers)
        response.raise_for_status()
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{API_ENDPOINT}/{city['id']}",
                json=new_data
            )
            response.raise_for_status()
            print(response.text)
