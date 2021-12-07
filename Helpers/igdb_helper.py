import igdb.wrapper as igdb
import json
import os
#"0jaadee4h3da3t26mebogxdwemcin5", "tvr6j1be97za7if28gvtqdm1fjlay8"


def create_wrapper(client_id, app_access_token):
    igdb_wrapper = igdb.IGDBWrapper(client_id, app_access_token)
    return igdb_wrapper


def create_api_request(igdb_wrapper, endpoint, data):
    igdb_api_response = igdb_wrapper.api_request(endpoint, data)
    return convert_to_json(igdb_api_response)


def convert_to_json(bytes_array):
    return bytes_array
