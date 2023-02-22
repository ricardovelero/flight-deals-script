import requests
import os
from flight_data import FlightData

API_ENDPOINT = "https://api.tequila.kiwi.com"
API_SEARCH = "/v2/search"
API_KEY = os.environ.get("TEQUILA_AUTH_TOKEN")

headers = {
    "apikey": API_KEY,
    "accept": "application/json"
}


class FlightSearch:

    def flight_search(self, origin_code, destination_code, from_time, to_time,):
        search_params = {
            "fly_from": origin_code,
            "fly_to": destination_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR"
        }
        response = requests.get(
            url=API_ENDPOINT+API_SEARCH, headers=headers, params=search_params)
        response.raise_for_status()

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: €{flight_data.price}")
        return flight_data

    def get_destination_code(self, city_name):
        query = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=f"{API_ENDPOINT}/locations/query",
                                headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code
