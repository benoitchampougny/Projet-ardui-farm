from architect.models import Network

def get_class_by_name(component_type):
    return getattr(Network, component_type)
