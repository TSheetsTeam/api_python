from tsheets.model import Model
from datetime import date, datetime


class LastModifiedTimestamps(Model):
    pass

LastModifiedTimestamps.add_default_type(datetime)
