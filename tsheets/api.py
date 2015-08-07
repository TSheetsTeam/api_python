import requests
from repository import UserRepository
from config import Config
from bridge import Bridge
import logger


class TSheets:
    repos = [{"name": "users", "class": UserRepository}]

    def __init__(self, access_token):
        self.config = Config(access_token)
        self.bridge = Bridge(self.config)
        self.cache = None
        for repo in TSheets.repos:
            setattr(self, repo["name"], repo["class"](self.bridge, self.cache))

