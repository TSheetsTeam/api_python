from tsheets.model import Model
from datetime import date, datetime


class Jobcode(Model):
    pass


Jobcode.add_field("id", int)
Jobcode.add_field("parent_id", int)
Jobcode.add_field("name", str)
Jobcode.add_field("short_code", str)
Jobcode.add_field("type", str)
Jobcode.add_field("billable", bool)
Jobcode.add_field("billable_rate", float)
Jobcode.add_field("has_children", bool)
Jobcode.add_field("assigned_to_all", bool)
Jobcode.add_field("required_customfields", [int])
Jobcode.add_field("filtered_customfielditems", object)
Jobcode.add_field("active", bool)
Jobcode.add_field("last_modified", datetime)
Jobcode.add_field("created", datetime)
