from tsheets.model import Model
from datetime import date, datetime


class JobcodeAssignment(Model):
    pass


JobcodeAssignment.add_field("id", int)
JobcodeAssignment.add_field("user_id", int)
JobcodeAssignment.add_field("jobcode_id", int)
JobcodeAssignment.add_field("active", bool)
JobcodeAssignment.add_field("last_modified", datetime)
JobcodeAssignment.add_field("created", datetime)
