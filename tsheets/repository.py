import dateutil
from results import Results
from datetime import date, datetime
from error import FilterInvalidValueError, MethodNotAvailableError


class Repository(object):
    filters = {}
    inherited_classes = []

    def __init__(self, bridge):
        self.bridge = bridge

    def where(self, **options):
        if self.validate_actions("list"):
            return Results(self.url, self.validated_options(options), self, self.bridge, self.is_singleton)

    def report(self, **options):
        if self.validate_actions("report"):
            return Results(self.url, self.validated_options(options), self.model, self.bridge, self.is_singleton, "report")

    def first(self):
        return self.where().next()

    def all(self):
        return self.where().all()

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
                    if not isinstance(value, type_of_filter):
                        raise FilterInvalidValueError("Expected the value for the {} filter to "
                                                      "match the given type: {}".format(name, type_of_filter))
                    if type_of_filter == datetime or type_of_filter == date:
                        #options[name] = str(value)
                        pass
            else:
                raise FilterInvalidValueError("Unknown Filter for class - {} filter - {}".format(self.__class__, name))
        return options

    def validate_actions(self, action):
        if action in self.actions:
            return True
        else:
            raise MethodNotAvailableError("Method '{}' not available on {} due to lack of the {} in available actions "
                                          "list. Actions list: {}".format(action, self.__class__.__name__, action, self.actions))

    def insert(self, entity):
        if self.validate_actions("add"):
            return self.bridge.insert(self.url, entity.to_raw("add"))

    def update(self, entity):
        if self.validate_actions("edit"):
            return self.bridge.update(self.url, entity.to_raw("edit"))

    def delete(self, entity):
        if self.validate_actions("delete"):
            return self.bridge.delete(self.url, entity.id)

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
        cls.is_singleton = options.get("singleton", False)

    @classmethod
    def add_url(cls, url):
        cls.url = url