from tsheets.repository import Repository
from datetime import date, datetime
import tsheets.models as models


class CurrentUser(Repository):
    pass


CurrentUser.add_me_to_subcls()
CurrentUser.add_url("/current_user")
CurrentUser.add_model(models.User)
CurrentUser.add_actions(['list'])
