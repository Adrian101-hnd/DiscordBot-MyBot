import os
from steam import Steam
import requests
import json
from dotenv import load_dotenv
load_dotenv()

KEY = os.environ.get("STEAM_API_KEY")
steam = Steam(KEY)


game_name = "Terraria"

class steam_fn():

    def game_search(game_name):
        dictionary = steam.apps.search_games(game_name)
        	
        dict_apps = dictionary["apps"]
        dict_id = dict_apps[0]
        app_id = dict_id["id"]
        return(str (app_id))


    def game_details(app_id):
        steam.apps.get_app_details(app_id)

    def player_count(app_id,game_name):
        header = {"Client-ID": KEY }

        game_players_url = 'https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?format=json&appid=' + app_id
        game_players = requests.get(game_players_url, headers=header)

        print("Game name:"+ game_name + ", Player count: " + str(game_players.json()['response']['player_count']))


app_id = steam_fn.game_search(game_name)
print(steam_fn.player_count(app_id))







