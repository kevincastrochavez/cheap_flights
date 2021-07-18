from pprint import pprint
import requests

OWN_GOOGLE_SHEET_API = 'https://api.sheety.co/6ada9ef7386080ce9ab42b293d2f77d5/flightDeals/prices'


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=OWN_GOOGLE_SHEET_API)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{OWN_GOOGLE_SHEET_API}/{city['id']}",
                json=new_data
            )
            print(response.text)
