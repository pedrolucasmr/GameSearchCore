from models import search
import os
import json


class SearchManager:

    def __init__(self, search_repository, result_repository, data_manager, filter_manager, igdb_manager):
        self._search_repository = search_repository
        self._result_repository = result_repository
        self._data_manager = data_manager
        self._filter_manager = filter_manager
        self._igdb_manager = igdb_manager

    def create_search(self, search_content):
        new_search = self.map_search_object(search_content)

        if self._search_repository.get_search_by_id(new_search.id) is not None:
            result = self._result_repository.get_result_by_search_id
            if result is not None:
                return result
            self._search_repository.update_search_date(new_search.id, new_search.created_at)

        result = self.map_result_object(
            self._igdb_manager.create_api_request(
                self._igdb_manager.create_wrapper(os.getenv("CLIENT_ID"), os.getenv("APP_ACCESS_TOKEN")),
                "games",
                self._filter_manager.create_filter(new_search)))

        result = self._data_manager.handle_result(result)
        self._result_repository.insert(result)

        return result

    def map_result_object(self, result_content):
        return ""

    def map_search_object(self, search_content):
        return search(
            search_content[0].id,
            search_content[0].created_at,
            search_content[0].genres,
            search_content[0].titles,
            search_content[0].platforms,
            search_content[0].developers,
            search_content[0].relase_years)
