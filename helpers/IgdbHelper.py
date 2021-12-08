@staticmethod
class IgdbHelper:

    @staticmethod
    def create_wrapper(client_id, app_access_token, igdb):
        igdb_wrapper = igdb.IGDBWrapper(client_id, app_access_token)
        return igdb_wrapper

    @staticmethod
    def create_api_request(igdb_wrapper, endpoint, data, json):
        igdb_api_response = igdb_wrapper.api_request(endpoint, data)
        return json.load(igdb_api_response)
