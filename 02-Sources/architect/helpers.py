from architect.models import Network
from architect.models import Location

def get_class_by_name(component_type):
    return getattr(Network, component_type)

def get_class_location_by_name(component_type):
    return getattr(Location, component_type)
