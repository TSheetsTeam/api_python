from tsheets.model import Model
from datetime import date, datetime


class CustomField(Model):
    pass


CustomField.add_field("id", int)
CustomField.add_field("active", bool)
CustomField.add_field("name", str)
CustomField.add_field("short_code", str)
CustomField.add_field("required", bool)
CustomField.add_field("applies_to", str)
CustomField.add_field("type", str)
CustomField.add_field("ui_preference", str)
CustomField.add_field("regex_filter", str)
CustomField.add_field("last_modified", datetime)
CustomField.add_field("created", datetime)
CustomField.add_field("required_customfields", [int])
