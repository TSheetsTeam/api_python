from tsheets.model import Model
from datetime import date, datetime


class Reminder(Model):
    pass


Reminder.add_field("id", int)
Reminder.add_field("user_id", int)
Reminder.add_field("reminder_type", str)
Reminder.add_field("due_time", str)
Reminder.add_field("due_days_of_week", str)
Reminder.add_field("distribution_methods", [str])
Reminder.add_field("active", bool)
Reminder.add_field("enabled", bool)
Reminder.add_field("last_modified", datetime)
Reminder.add_field("created", datetime)
