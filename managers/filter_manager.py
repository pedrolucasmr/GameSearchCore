class FilterManager:
    from helpers.igdb_helper import IgdbHelper
    import os

    wrapper = IgdbHelper.create_wrapper(os.getenv("CLIENT_ID"), os.getenv("APP_ACCESS_TOKEN"))

    def create_filter(self, content):
        pass

    def get_genre_id(self):
        self.IgdbHelper.create_api_request(
            self.wrapper,
            "genres",
            "fields name, checksum"
    )