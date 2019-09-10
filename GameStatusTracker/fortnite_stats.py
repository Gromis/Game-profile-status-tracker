import json
import requests
from operator import itemgetter

class Fortnite():
    def __init__(self, platform = 'pc'):
        self.api_key = '5f1c8da2-a843-479e-84af-4e2be4a50a95'
        self.platform = platform
        self.fortnite_url = 'https://api.fortnitetracker.com/v1/profile/pc/'
        self.headers = {
            'content-type': "application/json",
            'TRN-API-KEY': self.api_key,
          }

    def playerGet(self, player_handle):

        response = requests.request("GET",'https://api.fortnitetracker.com/v1/profile/pc/' + str(player_handle.strip(" ")), headers=self.headers)
        data = response.json()
        self.p2_data = data['stats']['p2']
        value_getter = itemgetter('displayValue')
        self.p2_data = {key: value_getter(value) for key, value in self.p2_data.items()}

    def playerStats(self):
        return self.p2_data