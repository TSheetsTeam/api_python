from tsheets.model import Model
from datetime import date, datetime


class EffectiveSettings(Model):
    pass


EffectiveSettings.add_field("general", dict)
EffectiveSettings.add_field("time_entry", dict)
EffectiveSettings.add_field("invoicing", dict)
EffectiveSettings.add_field("alerts", dict)
EffectiveSettings.add_field("dialin", dict)
EffectiveSettings.add_field("sounds", dict)
