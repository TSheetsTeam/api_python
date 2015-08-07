class Model(object):
    accessors = {}

    def __init__(self, hash = None, options = {}):
        self._dynamic_accessors = []
        if hash:
            self.__class__.mass_assign(self, hash, {})

    def add_field(self, fname, type_f, options={}):
        setattr(self, fname, None)
        if not self.__class__.accessors:
            self.__class__.accessors[self.__class__] = []
        exclude = options.get('exclude', [])
        self.__class__.accessors[self.__class__].append({'name': fname, 'type': type_f, 'exclude': exclude})

    @classmethod
    def from_raw(cls, hash):
        instance = cls()
        return cls.mass_assign(instance, hash)

    @classmethod
    def mass_assign(cls, instance, hash):
        dynamic = instance._dynamic_accessors

        for k,v in hash.iteritems():
            casted = cls.cast_raw(v, k)
            if hasattr(instance, k):
                setattr(instance, k, casted)
            else:
                setattr(instance, k, casted)
                dynamic.append({'name': k})
        instance._dynamic_accessors = dynamic

        return instance

    @classmethod
    def cast_raw(cls, value, key):



