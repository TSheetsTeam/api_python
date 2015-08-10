from tsheets.model import Model
from datetime import date, datetime


class Timesheet(Model):
    pass


Timesheet.add_field("id", int, {"exclude": ['add', 'edit']})
Timesheet.add_field("user_id", int)
Timesheet.add_field("jobcode_id", int)
Timesheet.add_field("locked", int, {"exclude": ['add', 'edit']})
Timesheet.add_field("notes", str)
Timesheet.add_field("customfields", str)
Timesheet.add_field("created", datetime)
Timesheet.add_field("last_modified", datetime)
Timesheet.add_field("type", str)
Timesheet.add_field("on_the_clock", bool, {"exclude": ['add', 'edit']})
Timesheet.add_field("start", datetime)
Timesheet.add_field("end", datetime)
Timesheet.add_field("date", date)
Timesheet.add_field("duration", int)
Timesheet.add_field("tz", int, {"exclude": ['add', 'edit']})
Timesheet.add_field("tz_str", str, {"exclude": ['add', 'edit']})
Timesheet.add_field("location", str, {"exclude": ['add', 'edit']})
