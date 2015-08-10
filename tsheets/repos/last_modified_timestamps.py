from tsheets.repository import Repository
from datetime import date, datetime
import tsheets.models as models


class LastModifiedTimestamps(Repository):
    pass


LastModifiedTimestamps.add_me_to_subcls()
LastModifiedTimestamps.add_url("/last_modified_timestamps")
LastModifiedTimestamps.add_model(models.LastModifiedTimestamps, singleton=True)
LastModifiedTimestamps.add_actions([u'list'])
