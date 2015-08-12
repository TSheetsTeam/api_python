from models.user import User
from results import Results
import dateutil
from error import FilterInvalidValueError
from datetime import date, datetime
import pytz


class Repository(object):
    filters = {}
    inherited_classes = []

    def __init__(self, bridge):
        self.bridge = bridge

    def where(self, **options):
        if "list" in self.actions:
            return Results(self.url, self.validated_options(options), self.model, self.bridge, self.is_singleton)

    def validated_options(self, options):
        for name, value in options.iteritems():
            if name in Repository.filters:
                type_of_filter = Repository.filters[name]
                if isinstance(type_of_filter, list):
                    if not isinstance(value, list):
                        raise FilterInvalidValueError("Expected the value of {} filter to be an list".format(name))
                    else:
                        for i in value:
                            if not isinstance(i, type_of_filter[0]):
                                raise FilterInvalidValueError("Expected all the values of a list for the {} filter to "
                                                              "match the given type {}".format(name, type_of_filter))
                else:
                    if type_of_filter == datetime or type_of_filter == date:
                        dt = self.validate_datetime(value, type_of_filter)
                        options[name] = str(dt)
                    if not isinstance(value, type_of_filter):
                        raise FilterInvalidValueError("Expected the value for the {} filter to "
                                                      "match the given type: {}".format(name, type_of_filter))
            else:
                raise FilterInvalidValueError("Unknown Filter for class - {} filter - {}".format(self.__class__, name))

    def validate_datetime(self, value, type_of_filter):
        try:
            value_with_tz = ""
            dt = dateutil.parser.parse(value)
            if not dt.tzinfo:
               value_with_tz = value.replace(tzinfo=pytz.UTC)
            return value_with_tz
        except:
            if type_of_filter == "datetime":
                raise FilterInvalidValueError("Expected datetime is String (ISO8601 format) "
                                              "ie: (i.e. 2004-02-12T15:19:21+00:00)")
            raise FilterInvalidValueError("Expected date format is String. YYYY-MM-DD formatted date. "
                                          "ie: (i.e. 2004-02-12)")

    @classmethod
    def add_me_to_subcls(cls):
        Repository.inherited_classes.append(cls)

    @classmethod
    def filter(cls, fname, type):
        Repository.filters[fname] = type

    @classmethod
    def add_actions(cls, action_list):
        cls.actions = action_list

    @classmethod
    def add_model(cls, model, **options):
        cls.model = model
        print options
        cls.is_singleton = options.get("singleton", False)
        print cls.is_singleton

    @classmethod
    def add_url(cls, url):
        cls.url = url