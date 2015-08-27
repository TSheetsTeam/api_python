:exclamation::exclamation:TSheets Python API Helper is currently under development, not ready for general use:exclamation::exclamation:

# TSheets API - Python client library

This client library provides access to the REST API exposed by the TSheets.com.

# Usage

Below examples assume that you properly added the tsheets library into your pip requirements.txt or have loaded the library in any other way.

## Authentication

TSheets platform uses OAuth2 for authentication. Because of the character of the library, it doesn't deal with the process of obtaining the authentication token needed for the OAuth2 protocol. You can find information about obtaining the token statically via the application's interface here: [https://developers.tsheets.com/docs/api/authentication]()

Once the auth token is obtained, a user has to create the 'api' instance object e.g:

```python
from tsheets import TSheets
api = TSheets("authtoken")
```

## Basics

The 'api' instance gives access to different resource end points e. g:

```python
api.timesheets.where(start_date = some_start, end_date = some_end)
```

The 'timesheets' method returns an instance of the timesheets end point repository. Repositories are means of communication with the TSheets API. They provide ways of fetching data as well as updating, inserting or deleting.

### Fetching data

The above example returns a "lazy query" - it doesn't connect with the TSheets API unless you need to get the resulting items out if it. Because such queries are Python iterables. To get all the items at once:

```python
list_of_results = api.timesheets.where(start_date=some_start, end_date=some_end).all()
for item in list_of_results:
    print item
```

One could also fetch only the first 10 with:

```python
list_of_results = api.timesheets.where(start_date=some_start, end_date=some_end)
for item in range(10):
    print list_of_results.next()
```

Some of the end points will always yield at most one result. In such case it's handy to just use:

```python
# The current_user end point returns a User
api.current_user.first()
```

### Inserting new data

Some end points permit insertion of new data. This is accomplished with e. g:

```python
from tsheets.models import Timesheet
timesheet = Timesheet(user_id= 1, type= 'manual', date= '2015-05-05', duration= 5500, jobcode_id=0)
result = api.timesheets.insert(t)
```


The 'result' variable there contains the context info about the operation. You can check if it went well with:

```python
if result.is_success():
    # some logic here
```

In case it didn't went well, you can obtain the useful explanation with:

```python
if !result.is_success():
    print result.message
```

At any point you can grab the resulting JSON with:

```python
result.body
```

### Updating data

Updates are being done in the same way as inserts. You just need to use the **update** method instead:

```python
result = api.someendpoint.update(some_object)
if result.is_success():
  print 'Yay!'
else:
  print "Error: #{result.message}"
```

### Deletes

Deletes follow the same pattern as inserts and updates:

```python
result = api.someendpoint.delete(some_object)
if result.is_success():
  print 'Gone for good!'
else
  print "Error: {}".format(result.message)
end
```

### Specifics

All information about possible filters one can pass to **where**, or required when inserting or updating are available e. g: [https://developers.tsheets.com/docs/api/]()

## Reports

There are three report types one can ask the API for. Fetching them follows the same pattern as normal fetches with **where**, only difference being the **report** method that's being in use e. g:

```python
from datetime import date
api.payroll.report(start_date=date(2015,01,01), end_date=date(2015,12,12)).first()
```
