from tsheets.model import Model
from datetime import date, datetime


class UserPermissionsSet(Model):
    pass


UserPermissionsSet.add_field("admin", bool)
UserPermissionsSet.add_field("mobile", bool)
UserPermissionsSet.add_field("status_box", bool)
UserPermissionsSet.add_field("reports", bool)
UserPermissionsSet.add_field("manage_timesheets", bool)
UserPermissionsSet.add_field("manage_authorization", bool)
UserPermissionsSet.add_field("manage_users", bool)
UserPermissionsSet.add_field("manage_my_timesheets", bool)
UserPermissionsSet.add_field("manage_jobcodes", bool)
UserPermissionsSet.add_field("approve_timesheets", bool)
