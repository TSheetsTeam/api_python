import requests
from models.user import User
from repository import UserRepository
from http_client import HTTPClient

class TSheets:
    def __init__(self, access_token):
        self._client = HTTPClient(access_token = access_token)
        self.users = UserRepository(self._client)
