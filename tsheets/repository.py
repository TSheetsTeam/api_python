from models.user import User
from results import Results


class Repository(object):
    print "Repository class creation"
    filters = {}
    inherited_classes = []

    def __init__(self, bridge):
        self.bridge = bridge

    def where(self, options={}):
        if "list" in self.actions:
            return Results(self.url, self.validated_options(options), self.model, self.bridge, self.is_singleton)

    def validated_options(self, options={}):
        for name, value in options.iteritems():
            if name in Repository.filters:
                type_of_filter = Repository.filters[name]
                if isinstance(type_of_filter, list):
                    if not isinstance(value, list):
                        # todo
                        pass
                    else:
                        for i in value:
                            if not isinstance(i, type_of_filter[0]):
                                # todo raise exception
                                print "Exception"
                else:
                    if not isinstance(value, type_of_filter):
                        print "Exception"
                        # todo
            else:
                # todo
                print "Exception"
        return options

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
    def add_model(cls, model, options={}):
        cls.model = model
        cls.is_singleton = options.get("singleton", False)

    @classmethod
    def add_url(cls, url):
        cls.url = url
