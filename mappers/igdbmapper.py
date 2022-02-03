class igdbMapper:
    def map_list_filter(self, fields, limit=5):
        result_filter = self.map_field_list(fields)
        result_filter = result_filter + " limit " + str(limit) + ";"
        return result_filter

    def map_search_filter(self, search_condition, fields, limit=5):
        result_filter = self.map_field_list(fields)
        result_filter = result_filter + " search " + '"' + search_condition + '"' + ";"
        result_filter = result_filter + " limit " + str(limit) + ";"
        return result_filter

    def map_field_list(self, fields):
        result_filter = "fields "
        for field in fields:
            result_filter = result_filter + field + ","
        result_filter = result_filter[:-1] + ";"
        return result_filter

    def map_response_to_object(self, response):

