from tsheets.repository import Repository
from datetime import date, datetime
import tsheets.models as models


class JobcodeAssignments(Repository):
    pass


JobcodeAssignments.add_me_to_subcls()
JobcodeAssignments.add_url("/jobcode_assignments")
JobcodeAssignments.add_model(models.JobcodeAssignment)
JobcodeAssignments.add_actions(['list', 'add', 'delete'])
JobcodeAssignments.filter("user_ids", [int])
JobcodeAssignments.filter("type", str)
JobcodeAssignments.filter("jobcode_parent_id", int)
JobcodeAssignments.filter("active", str)
JobcodeAssignments.filter("modified_before", datetime)
JobcodeAssignments.filter("modified_since", datetime)
JobcodeAssignments.filter("per_page", int)
JobcodeAssignments.filter("page", int)
