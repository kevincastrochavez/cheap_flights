import requests

# OWN_GOOGLE_SHEET_API = 'https://api.sheety.co/6ada9ef7386080ce9ab42b293d2f77d5/flightDeals/prices'

class DataManager:
    def __init__(self):
        self.destination = {}
    
    def get_destination_data(self):
        response = requests.get(url=OWN_GOOGLE_SHEET_API)
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data