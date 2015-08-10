from tsheets.repository import Repository
from datetime import date, datetime
import tsheets.models as models


class CustomFieldItems(Repository):
    pass


CustomFieldItems.add_me_to_subcls()
CustomFieldItems.add_url("/customfielditems")
CustomFieldItems.add_model(models.CustomFieldItem)
CustomFieldItems.add_actions([u'list', u'add', u'edit'])
CustomFieldItems.filter("customfield_id", int)
CustomFieldItems.filter("ids", [int])
CustomFieldItems.filter("active", str)
CustomFieldItems.filter("modified_before", datetime)
CustomFieldItems.filter("modified_since", datetime)
CustomFieldItems.filter("per_page", int)
CustomFieldItems.filter("page", int)
