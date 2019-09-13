from tsheets.repository import Repository
from datetime import date, datetime
import tsheets.models as models


class CustomFields(Repository):
    pass


CustomFields.add_me_to_subcls()
CustomFields.add_url("/customfields")
CustomFields.add_model(models.CustomField)
CustomFields.add_actions(['list'])
CustomFields.filter("ids", [int])
CustomFields.filter("active", bool)
CustomFields.filter("applies_to", str)
CustomFields.filter("value_type", str)
CustomFields.filter("modified_before", str)
CustomFields.filter("modified_since", str)
CustomFields.filter("per_page", int)
CustomFields.filter("page", int)
