from tsheets.model import Model
from datetime import date, datetime


class Notification(Model):
    pass


Notification.add_field("id", int)
Notification.add_field("user_id", int)
Notification.add_field("msg_tracking_id", str)
Notification.add_field("message", str)
Notification.add_field("method", str)
Notification.add_field("precheck", str)
Notification.add_field("delivery_time", datetime)
Notification.add_field("created", date)
