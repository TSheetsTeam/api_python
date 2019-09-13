from tsheets.repository import Repository
from datetime import date, datetime
import tsheets.models as models


class TimesheetsDeleted(Repository):
    pass


TimesheetsDeleted.add_me_to_subcls()
TimesheetsDeleted.add_url("/timesheets_deleted")
TimesheetsDeleted.add_model(models.TimesheetDeleted)
TimesheetsDeleted.add_actions(['list'])
TimesheetsDeleted.filter("start_date", date)
TimesheetsDeleted.filter("end_date", date)
TimesheetsDeleted.filter("ids", [int])
TimesheetsDeleted.filter("modified_since", datetime)
TimesheetsDeleted.filter("modified_before", datetime)
TimesheetsDeleted.filter("group_ids", str)
TimesheetsDeleted.filter("user_ids", [int])
TimesheetsDeleted.filter("username", str)
TimesheetsDeleted.filter("jobcode_ids", [int])
TimesheetsDeleted.filter("jobcode_type", str)
TimesheetsDeleted.filter("type", str)
TimesheetsDeleted.filter("order_results_by", str)
TimesheetsDeleted.filter("order_results_reverse", bool)
TimesheetsDeleted.filter("page", int)
TimesheetsDeleted.filter("per_page", int)
