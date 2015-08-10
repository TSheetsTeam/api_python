from tsheets.model import Model
from datetime import date, datetime


class CurrentTotals(Model):
    pass


CurrentTotals.add_field("user_id", int)
CurrentTotals.add_field("on_the_clock", bool)
CurrentTotals.add_field("timesheet_id", int)
CurrentTotals.add_field("jobcode_id", int)
CurrentTotals.add_field("group_id", int)
CurrentTotals.add_field("shift_seconds", int)
CurrentTotals.add_field("day_seconds", int)
