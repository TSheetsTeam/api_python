from tsheets.model import Model
from datetime import date, datetime


class Payroll(Model):
    pass


Payroll.add_field("user_id", int)
Payroll.add_field("client_id", int)
Payroll.add_field("start_date", date)
Payroll.add_field("end_date", date)
Payroll.add_field("total_re_seconds", int)
Payroll.add_field("total_ot_seconds", int)
Payroll.add_field("total_dt_seconds", int)
Payroll.add_field("total_pto_seconds", int)
Payroll.add_field("total_work_seconds", int)
Payroll.add_field("pto_seconds", dict)
