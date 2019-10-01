from tsheets.repository import Repository
from datetime import date, datetime
import tsheets.models as models


class CurrentTotals(Repository):
    pass


CurrentTotals.add_me_to_subcls()
CurrentTotals.add_url("/reports/current_totals")
CurrentTotals.add_model(models.CurrentTotals)
CurrentTotals.add_actions(['report'])
CurrentTotals.filter("user_ids", [int])
CurrentTotals.filter("group_ids", [int])
CurrentTotals.filter("on_the_clock", str)
CurrentTotals.filter("page", int)
CurrentTotals.filter("per_page", int)
CurrentTotals.filter("order_by", str)
CurrentTotals.filter("order_desc", bool)
