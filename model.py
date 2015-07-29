class Model(object):
    def __init__(self):
        self.accessors = {}
        pass

    def add_field(self, fname, type_of_f):
        setattr(self, fname, None)
        self.accessors[fname] = {'name':fname, 'type': type_of_f}

    @classmethod
    def from_raw(cls, json_response={}):
        o = cls.__init__()
        for k,v in json_response.iteritems():
            if k in o.accessors:
                o.k = v

        return o

