from tsheets.model import Model
from datetime import date, datetime


class TimesheetDeleted(Model):
    pass


TimesheetDeleted.add_field("id", int)
TimesheetDeleted.add_field("user_id", int)
TimesheetDeleted.add_field("jobcode_id", int)
TimesheetDeleted.add_field("start", datetime)
TimesheetDeleted.add_field("end", datetime)
TimesheetDeleted.add_field("date", date)
TimesheetDeleted.add_field("duration", int)
TimesheetDeleted.add_field("locked", int)
TimesheetDeleted.add_field("notes", str)
TimesheetDeleted.add_field("customfields", str)
TimesheetDeleted.add_field("created", datetime)
TimesheetDeleted.add_field("last_modified", datetime)
TimesheetDeleted.add_field("type", str)
