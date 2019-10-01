from tsheets.repository import Repository
from datetime import date, datetime
import tsheets.models as models


class Payroll(Repository):
    pass


Payroll.add_me_to_subcls()
Payroll.add_url("/reports/payroll")
Payroll.add_model(models.Payroll)
Payroll.add_actions(['report'])
Payroll.filter("start_date", date)
Payroll.filter("end_date", date)
Payroll.filter("user_ids", int)
Payroll.filter("group_ids", int)
Payroll.filter("include_zero_time", str)
