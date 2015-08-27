import helpers
import dateutil.parser
from datetime import datetime, date

class Model(object):
    _accessors = {}
    _default_type = "anything"

    def __init__(self, **kwargs):
        self._dynamic_accessors = []
        if kwargs:
            self.__class__.mass_assign(self, kwargs)

    @classmethod
    def add_field(cls, fname, type_f, options={}):
        setattr(cls, fname, None)
        if cls not in Model._accessors:
            Model._accessors[cls] = []
        exclude = options.get('exclude', [])
        Model._accessors[cls].append({'name': fname, 'type': type_f, 'exclude': exclude})

    @classmethod
    def add_default_type(cls, data_type):
        cls._default_type = data_type

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
    def type_for(cls, field_name):
        accessor = Model._accessors.get(cls, [])
        for i in accessor:
            if i["name"] == field_name:
                return i["type"]
        return cls._default_type

    @classmethod
    def type_for_key(cls, key):
        return cls.type_for(key)

    @classmethod
    def cast_raw(cls, value, key, type=None):
        if value is None:
            return None
        if type:
            type_symbol = type
        else:
            type_symbol = cls.type_for_key(key)

        if isinstance(type_symbol, list):
            value = [cls.cast_raw(i, key, type_symbol[0]) for i in value]
            return value
        elif type_symbol == str:
            return value
        elif type_symbol == int:
            return int(value)
        elif type_symbol == datetime:
            try:
                return dateutil.parser.parse(value)
            except:
                return None
        elif type_symbol == date:
            try:
                return datetime.strptime(value, "%Y-%m-%d").date()
            except:
                return None
        elif type_symbol == bool:
            return value == True
        elif type_symbol == dict:
            return value
        elif type_symbol == float:
            return float(value)
        elif type_symbol == object:
            if not value:
                return {}
            return value
        elif type_symbol == "anything":
            return value
        else:
            return helpers.to_class(type_symbol)().from_raw(value)

    def cast_to_raw(self, value, key, type = None):
        type_symbol = type or self.__class__.type_for_key(key)
        if isinstance(type_symbol, list):
            value = [self.cast_to_raw(i, key, type_symbol[0]) for i in value]
            return value
        elif type_symbol == str:
            return value
        elif type_symbol == int:
            return value
        elif type_symbol == datetime:
            if not value:
                return ""
            try:
                return value.isoformat()
            except:
                return None
        elif type_symbol == date:
            if not value:
                return ""
            try:
                return value.strftime("%Y-%m-%d")
            except:
                return None
        elif type_symbol == bool:
            return value
        elif type_symbol == dict:
            return value
        elif type_symbol == float:
            return value
        elif type_symbol == object:
            if not value:
                return ""
            return value
        elif type_symbol == "anything":
            return value
        else:
            if not value:
                return None
            return value.to_raw()

    def to_raw(self, mode=None):
        attributes = self.get_attributes(mode)
        obj = {}
        for k, v in attributes.iteritems():
            obj[k] = self.cast_to_raw(v, k)
        return obj

    def allowed_for_mode(self, mode, acc):
        return (mode is None) or (not bool(acc['exclude'])) or not (mode in acc['exclude'])

    def attribute_for_accessors(self, accessor):
        sum = {}
        for acc in accessor:
            sum[acc['name']] = self.__getattribute__(acc['name'])
        return sum

    def get_attributes(self, mode=None):
        _accessors = Model._accessors[self.__class__] if self.__class__ in Model._accessors else []
        acc = [a for a in _accessors if self.allowed_for_mode(mode, a)]

        acc = []
        for a in _accessors:
            if self.allowed_for_mode(mode, a):

                acc.append(a)
        return self.attribute_for_accessors(acc)


