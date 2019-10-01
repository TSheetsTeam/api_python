from tsheets.repository import Repository
from datetime import date, datetime
import tsheets.models as models


class Jobcodes(Repository):
    pass


Jobcodes.add_me_to_subcls()
Jobcodes.add_url("/jobcodes")
Jobcodes.add_model(models.Jobcode)
Jobcodes.add_actions(['list', 'add', 'edit'])
Jobcodes.filter("ids", [int])
Jobcodes.filter("parent_ids", [int])
Jobcodes.filter("type", str)
Jobcodes.filter("active", str)
Jobcodes.filter("modified_before", datetime)
Jobcodes.filter("modified_since", datetime)
Jobcodes.filter("per_page", int)
Jobcodes.filter("page", int)
