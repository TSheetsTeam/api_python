from tsheets.repository import Repository
from tsheets.models import *
import datetime

class Users(Repository):
    pass

Users.add_me_to_subcls()
Users.add_url("/users")
Users.add_model(User)
Users.add_actions(["list", "add", "edit"])
Users.filter("ids", [int])
Users.filter("usernames", [str])
Users.filter("active", bool)
Users.filter("first_name", str)
Users.filter("last_name", str)
Users.filter("modified_before", datetime.datetime)
Users.filter("modified_since", datetime.datetime)
Users.filter("per_page",int)
Users.filter("page", int)