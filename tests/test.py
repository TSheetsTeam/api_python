import os
import sys
import inspect
import argparse
from datetime import date, datetime

ARGS = None

cmd_folder = os.path.abspath(os.path.join(os.path.split(inspect.getfile(
    inspect.currentframe()))[0], ".."))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

from tsheets.api import TSheets
from tsheets.models import Timesheet

def parse_args():
    """
    Simple argument parser
    """
    parser = argparse.ArgumentParser(
            description='basic tests for tsheets production api service')
    parser.add_argument('-a', '--auth', type=str, help='auth token to access the production api service')
    r = parser.parse_args()
    if not r.auth:
        parser.error("You need to specify the access token to connect to a real TSheets service")
    return r


def main():
    global ARGS
    ARGS = parse_args()

    api = TSheets(ARGS.auth)

    # who am i?
    current_user = api.current_user.first()
    user_id = current_user.id

    print("Successfully connected to TSheets. Grabbed the current user's id: {}".format(user_id))

    # Make sure we can pull last-modified, non-paginated
    last_modified = api.last_modified_timestamps.where(endpoints='timesheets')
    print("Found timestamp for timesheets: {}".format(last_modified.first().timesheets))

    # get a list of job codes
    my_jobcode = None
    jobcodes = api.jobcodes.where(type = 'regular', active = True)
    for jobcode in jobcodes:
        if jobcode.name == 'Ancient Artifacts Inc.':
            my_jobcode = jobcode

    if not my_jobcode:
        print("No jobcode named 'Ancient Artifacts Inc.' found. " \
              "Make sure you have that created for your account for this test to continue")

    print(" - Selecting Jobcode {}".format(my_jobcode.name))

    # check to see if I am already on the clock
    timesheet = None
    timesheets = api.timesheets.where(modified_since=datetime(2015,7,1), on_the_clock = True, user_ids=[current_user.id]).all()
    if len(timesheets) > 0:
        print(' - Already clocked-in')
        timesheet = timesheets[0]
        print(timesheet)
    else:
        print(' - Not clocked-in')

    # Toggle clock-in or clock-out
    if timesheet == None:
        print(' - Clocking in')

        # create a new timesheet
        timesheet = Timesheet()
        timesheet.type = 'regular'
        timesheet.start = datetime.now()
        timesheet.end = None
        timesheet.user_id = user_id
        timesheet.jobcode_id = my_jobcode.id
        result = api.timesheets.insert(timesheet)
        if not result.is_success():
            print(result.message())
    else:
        print(' - Clocking out')
        # edit existing timesheet
        timesheet.end = datetime.now()
        result = api.timesheets.update(timesheet)
        if not result.is_success():
            print(result.message())

if __name__ == '__main__':
    main()

