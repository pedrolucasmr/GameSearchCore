from managers.igdb_manager import IgdbManager
import os
import requests


def get_games_info():
    manager = IgdbManager(os.getenv("CLIENT_ID"), os.getenv("APP_ACCESS_TOKEN"))
    data = "fields name,aggregated_rating,category,checksum,franchise,genres,involved_companies,platforms,rating; limit 5;"
    response = manager.create_api_request(manager.create_wrapper(), "games", data)
    return response


def get_game_info(game_name):
    manager = IgdbManager(os.getenv("CLIENT_ID"), os.getenv("APP_ACCESS_TOKEN"))
    data = "fields name,aggregated_rating,category,checksum,franchise,genres,involved_companies,platforms,rating; search"+'"'+game_name+'"'+"; limit 5;"
    response = manager.create_api_request(manager.create_wrapper(), "games", data)
    return response


def get_genres_info():
    manager = IgdbManager(os.getenv("CLIENT_ID"), os.getenv("APP_ACCESS_TOKEN"))
    data = "fields name,checksum; limit 5;"
    response = manager.create_api_request(manager.create_wrapper(), "genres", data)
    return response