from architect.models import Network

def get_model_with_component_type(component_type):
    return getattr(Network, component_type)
