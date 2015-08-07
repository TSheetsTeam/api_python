import json
import urlparse
from error import TSheetsError


class Bridge(object):

    def __init__(self, config):
        self.config = config
        self.auth_options = { "Authorization" : "Bearer {}".format(self.config.access_token)}

    def items_from_data(self, data, name, is_singleton, mode):
        if mode == "report":
            objects = data["results"].values[0]
            return [] if not objects else objects.values

        if is_singleton or (not isinstance(data['results'][name], dict)):
            return data['results'][name]
        else:
            return data['results'][name].values

    def next_batch(self, url, name, options, is_singleton = False, mode = "list"):
        method = "get" if mode == "list" else "post"

        if mode == "report":
            options = {"data": 0 if not options else options}

        if method == "get":
            response = self.config.adapter.get(urlparse.urljoin(self.config.base_url, url), options, self.auth_options)
        else:
            response = self.config.adapter.post(urlparse.urljoin(self.config.base_url, url), options, self.auth_options)

        data = response.json()

        if response.status_code == 200:
            if not data:
                return {"items": [], "has_more": False, "supplemental": {} }
            else:
                s_dict = {}
                if data['supplemental_data']:
                  for key, value in data['supplemental_data'].iteritems():
                    s_dict[key] = value.values

                result = {"items": self.items_from_data(data, name, is_singleton, mode),
                          "has_more": (data["more"] == True),
                          "supplemental": s_dict}
                return result
        else:
            raise TSheetsError("Expectation Failed")

    def insert(self, url, raw_entity):
        response = self.config.adapter.post(urlparse.urljoin(self.config.base_url, url), {'data': [raw_entity]}, self.auth_options)
        return response

    def update(self, url, raw_entity):
        response = self.config.adapter.put(urlparse.urljoin(self.config.base_url, url), {'data': [raw_entity]}, self.auth_options)
        return response

    def delete(self, url, id):
        response = self.config.adapter.delete(urlparse.urljoin(self.config.base_url, url), {'ids': [id]}, self.auth_options)
        return response
