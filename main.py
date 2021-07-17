import requests
import json
from pprint import pprint

# OWN_GOOGLE_SHEET_API = 'https://api.sheety.co/6ada9ef7386080ce9ab42b293d2f77d5/flightDeals/prices'
FAKE_API = 'data.json'

def main():
    # response = requests.get(OWN_GOOGLE_SHEET_API)
    # response.raise_for_status()
    # flights_data = response.json()

    # print(flights_data)

    file = open('data.json')
    data = json.load(file)
    pprint(data)

main()

