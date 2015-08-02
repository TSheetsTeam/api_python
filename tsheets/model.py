class Model(object):
    def __init__(self):
        self.accessors = {}
        pass

    def add_field(self, fname, type_of_f):
        setattr(self, fname, None)
        self.accessors[fname] = {'name':fname, 'type': type_of_f}

    @classmethod
    def from_raw(cls, json_response={}):
        o = cls()
        for k,v in json_response.items():
            print k,v
            if k in o.accessors:
                print "yes"
                setattr(o, k, v)
                print o.email
        return o

