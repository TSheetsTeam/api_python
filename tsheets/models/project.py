from tsheets.model import Model
from datetime import date, datetime


class Project(Model):
    pass


Project.add_field("start_date", date)
Project.add_field("end_date", date)
Project.add_field("totals", dict)
