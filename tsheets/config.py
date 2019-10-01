from .rest_adapter import RestAdapter


class Config(object):
    def __init__(self, access_token):
        self.access_token = access_token
        self.base_url = "https://rest.tsheets.com/api/v1"
        self.adapter = RestAdapter()