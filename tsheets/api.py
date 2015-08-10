import requests
from tsheets.repository import Repository
from config import Config
from bridge import Bridge
from helpers import class_to_endpoint


class TSheets:
    repos = []
    for repo in Repository.inherited_classes:
        name = class_to_endpoint(repo.__name__)
        repos.append({"name": name, "class": repo})

    def __init__(self, access_token):
        self.config = Config(access_token)
        self.bridge = Bridge(self.config)
        self.cache = None
        for repo in TSheets.repos:
            print repo["name"]
            setattr(self, repo["name"], repo["class"](self.bridge))