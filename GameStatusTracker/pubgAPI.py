import json
import requests
from operator import itemgetter


class PUBG_API():
    def __init__(self, shard = 'pc-eu'):
        self.shard = shard
        self.url = "https://api.playbattlegrounds.com/shards/" + self.shard + '/' + 'players' + '/account.0e7e0695cd914d62b8767307f48bc23f' + '/seasons' + '/division.bro.official.2018-07'
        self.api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIyYTQwZDRkMC01YzlhLTAxMzYtNWFmZi0wMGFmNjY3OTJmZTAiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTMwMTQ2NTk0LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InN0dWRlbnRhcGlfcHJvamVjdCJ9.zO_m1J-q0Ebz45OiugwiUl0-f4QPdD5zQ9Sp3ntz078"
        self.headers = {
            "Authorization": 'Bearer ' + self.api_key,
            "Accept": "application/vnd.api+json"
          }

    def getPlayer(self,player_name):
        response = requests.request("GET", self.url, headers=self.headers)
        data = response.json()
        self.data = data['data']['attributes']['gameModeStats']['solo-fpp']

    def get_data(self):
        return self.data
