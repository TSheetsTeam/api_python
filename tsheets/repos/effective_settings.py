from tsheets.repository import Repository
from datetime import date, datetime
import tsheets.models as models


class EffectiveSettings(Repository):
    pass


EffectiveSettings.add_me_to_subcls()
EffectiveSettings.add_url("/effective_settings")
EffectiveSettings.add_model(models.EffectiveSettings, singleton=True)
EffectiveSettings.add_actions(['list'])
EffectiveSettings.filter("user_id", int)
EffectiveSettings.filter("modified_before", datetime)
EffectiveSettings.filter("modified_since", datetime)
