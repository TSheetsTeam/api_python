class Model(object):
    def __init__(self):
        self.accessors = {}
        pass

    def add_field(self, fname, type_of_f):
        setattr(self, fname, None)
        self.accessors[fname] = {'name':fname, 'type': type_of_f}
