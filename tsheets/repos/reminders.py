from tsheets.repository import Repository
from datetime import date, datetime
import tsheets.models as models


class Reminders(Repository):
    pass


Reminders.add_me_to_subcls()
Reminders.add_url("/reminders")
Reminders.add_model(models.Reminder)
Reminders.add_actions([u'list', u'add', u'edit'])
Reminders.filter("user_ids", [int])
Reminders.filter("reminder_types", [str])
Reminders.filter("modified_since", datetime)
