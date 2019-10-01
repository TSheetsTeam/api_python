from tsheets.repository import Repository
from datetime import date, datetime
import tsheets.models as models


class Timesheets(Repository):
    pass


Timesheets.add_me_to_subcls()
Timesheets.add_url("/timesheets")
Timesheets.add_model(models.Timesheet)
Timesheets.add_actions(['list', 'add', 'edit', 'delete'])
Timesheets.filter("ids", [int])
Timesheets.filter("start_date", date)
Timesheets.filter("end_date", date)
Timesheets.filter("jobcode_ids", [int])
Timesheets.filter("user_ids", [int])
Timesheets.filter("group_ids", [int])
Timesheets.filter("on_the_clock", bool)
Timesheets.filter("jobcode_type", str)
Timesheets.filter("modified_before", datetime)
Timesheets.filter("modified_since", datetime)
Timesheets.filter("per_page", int)
Timesheets.filter("page", int)
