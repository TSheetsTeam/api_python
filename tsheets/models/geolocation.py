from tsheets.model import Model
from datetime import date, datetime


class Geolocation(Model):
    pass


Geolocation.add_field("id", int)
Geolocation.add_field("user_id", int)
Geolocation.add_field("accuracy", int)
Geolocation.add_field("altitude", float)
Geolocation.add_field("latitude", float)
Geolocation.add_field("longitude", float)
Geolocation.add_field("speed", float)
Geolocation.add_field("heading", int)
Geolocation.add_field("source", str)
Geolocation.add_field("device_identifier", str)
Geolocation.add_field("created", datetime)
