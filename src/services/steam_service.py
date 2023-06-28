import os
from steam import Steam
import requests
import json
from dotenv import load_dotenv
load_dotenv()

# KEY = os.environ.get("STEAM_API_KEY")
# steam = Steam(KEY)


# game_name = "Terraria"

class steam_fn():

    def __init__(self, api_key):
        print("Steam initiated")
        self.steam = Steam(api_key)

    def game_search(self,game_name):
        dictionary = self.steam.apps.search_games(game_name)
        	
        dict_apps = dictionary["apps"]
        dict_id = dict_apps[0]
        app_id = dict_id["id"]
        return(str (app_id))


    def game_details(self,app_id):
        self.steam.apps.get_app_details(app_id)

    def player_count(self,app_id,game_name):
        header = {"Client-ID": os.environ.get("STEAM_API_KEY")}

        game_players_url = 'https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?format=json&appid=' + app_id
        game_players = requests.get(game_players_url, headers=header)

        #print("Game name:"+ game_name + ", Player count: " + str(game_players.json()['response']['player_count']))
        return(str(game_players.json()['response']['player_count']))









