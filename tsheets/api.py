import requests
from models.user import User
from repository import UserRepository
import logger

class TSheets:
    def __init__(self, access_token):
        self._client = HTTPClient(access_token = access_token)
        self.users = UserRepository(self._client)
