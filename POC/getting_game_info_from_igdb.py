from managers.igdb_manager import IgdbManager
import os
from mappers.igdbmapper import igdbMapper


def get_games_info():
    mapper = igdbMapper()
    manager = IgdbManager(os.getenv("CLIENT_ID"), os.getenv("APP_ACCESS_TOKEN"))
    field_list = ["name", "aggregated_rating", "category", "checksum", "franchise", "genres", "involved_companies", "platforms", "rating"]
    data = mapper.map_list_filter(fields=field_list, limit=3)
    response = manager.create_api_request(manager.create_wrapper(), "games", data)
    return response


def get_game_info(game_name):
    mapper = igdbMapper()
    manager = IgdbManager(os.getenv("CLIENT_ID"), os.getenv("APP_ACCESS_TOKEN"))
    field_list = ["name", "aggregated_rating", "category", "checksum", "franchise", "genres", "involved_companies",
                  "platforms", "rating"]
    data = mapper.map_search_filter(search_condition=game_name, fields=field_list, limit=3)
    response = manager.create_api_request(manager.create_wrapper(), "games", data)
    return response


def get_genres_info():
    manager = IgdbManager(os.getenv("CLIENT_ID"), os.getenv("APP_ACCESS_TOKEN"))
    data = "fields name,checksum; limit 5;"
    response = manager.create_api_request(manager.create_wrapper(), "genres", data)
    return response