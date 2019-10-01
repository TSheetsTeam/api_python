from tsheets.repository import Repository
from datetime import date, datetime
import tsheets.models as models


class Geolocations(Repository):
    pass


Geolocations.add_me_to_subcls()
Geolocations.add_url("/geolocations")
Geolocations.add_model(models.Geolocation)
Geolocations.add_actions(['list', 'add'])
Geolocations.filter("ids", [int])
Geolocations.filter("modified_before", datetime)
Geolocations.filter("modified_since", datetime)
Geolocations.filter("user_ids", [int])
Geolocations.filter("group_ids", [int])
Geolocations.filter("per_page", int)
Geolocations.filter("page", int)
