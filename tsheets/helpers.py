import re
from tsheets.models import *
import sys
import types
import tsheets
import importlib
print globals()


def get_class(kls):
    parts = kls.split('.')
    module = ".".join(parts[:-1])
    m = __import__( module )
    for comp in parts[1:]:
        m = getattr(m, comp)
    return m

def to_class(value):
    components = value.split('_')
    # We capitalize the first letter of each component
    # with the 'title' method and join them together.
    field = "".join(x.title() for x in components)
    field = "tsheets.models.{}.{}".format(value, field)
    return get_class(field)


def class_to_endpoint(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).replace('-', '_').lower()