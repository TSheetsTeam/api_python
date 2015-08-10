from tsheets.model import Model
from datetime import date, datetime


class CustomFieldItem(Model):
    pass


CustomFieldItem.add_field("id", int)
CustomFieldItem.add_field("customfield_id", int)
CustomFieldItem.add_field("name", str)
CustomFieldItem.add_field("short_code", str)
CustomFieldItem.add_field("active", bool)
CustomFieldItem.add_field("last_modified", datetime)
CustomFieldItem.add_field("created", datetime)
CustomFieldItem.add_field("required_customfields", [int])
