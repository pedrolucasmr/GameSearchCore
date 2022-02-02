import json
import requests
from igdb.wrapper import IGDBWrapper


class IgdbManager:

    def __init__(self, client_id, app_access_token):
        self.client_id = client_id
        self.app_access_token = app_access_token

    def create_wrapper(self, client_id=None, app_access_token=None):
        if client_id is None:
            client_id = self.client_id

        if app_access_token is None:
            app_access_token = self.app_access_token

        access_token = self.get_access_token(client_id, app_access_token)
        igdb_wrapper = IGDBWrapper(client_id, access_token["access_token"])
        return igdb_wrapper

    @staticmethod
    def create_api_request(igdb_wrapper, endpoint, data):
        try:
            igdb_api_response = igdb_wrapper.api_request(endpoint, data)
            return json.dumps(json.loads(igdb_api_response))

        except requests.HTTPError as error:
            print(error)
            return error

    @staticmethod
    def get_access_token(client_id, app_access_token):
        try:
            access_token_response = requests.post("https://id.twitch.tv/oauth2/token?client_id="+client_id+"&client_secret="+app_access_token+"&grant_type=client_credentials")
            return json.loads(access_token_response.content)

        except requests.HTTPError as error:
            print(error)
            return error
