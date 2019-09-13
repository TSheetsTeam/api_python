from tsheets.repository import Repository
from datetime import date, datetime
import tsheets.models as models


class Project(Repository):
    pass


Project.add_me_to_subcls()
Project.add_url("/reports/project")
Project.add_model(models.Project)
Project.add_actions(['report'])
Project.filter("start_date", date)
Project.filter("end_date", date)
Project.filter("user_ids", [int])
Project.filter("group_ids", [int])
Project.filter("jobcode_ids", [int])
Project.filter("jobcode_type", str)
Project.filter("customfielditems", dict)
