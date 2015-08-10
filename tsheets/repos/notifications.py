from tsheets.repository import Repository
from datetime import date, datetime
import tsheets.models as models


class Notifications(Repository):
    pass


Notifications.add_me_to_subcls()
Notifications.add_url("/notifications")
Notifications.add_model(models.Notification)
Notifications.add_actions([u'list', u'add', u'delete'])
Notifications.filter("ids", [int])
Notifications.filter("delivery_before", datetime)
Notifications.filter("delivery_after", datetime)
Notifications.filter("user_id", int)
Notifications.filter("msg_tracking_id", str)
Notifications.filter("per_page", int)
Notifications.filter("page", int)
