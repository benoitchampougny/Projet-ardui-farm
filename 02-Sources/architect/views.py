from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from architect.models.Network import *
from architect.helpers import get_model_with_component_type

def home(request):
    return HttpResponseRedirect(reverse('network'))


#####################################################################################################
#                       MAIN VIEW
#####################################################################################################
def network(request, component_type=None, component_id=None):
    network = Network.objects.first()
    if network is not None:
        masterElement = network.master
        if component_type is None:
            element = masterElement
        else:
            component_class = get_model_with_component_type(component_type)
            element = get_object_or_404(component_class, pk=component_id)
        return render(  request, 'network/network.html', {'masterElement': masterElement, "element": element})
    else:
        return HttpResponse()


#####################################################################################################
#                       COMPONENT DETAILS
#####################################################################################################
def component_detail(request, component_type, component_id):
    component_class = get_model_with_component_type(component_type)
    element = get_object_or_404(component_class, pk=component_id)
    return render(  request, 'network/component_detail.html', {"element": element})


#####################################################################################################
#                       CREATE COMPONENT
#####################################################################################################
def create_component(request):
    if request.method == 'POST':
        # Retrieve form parameters
        component_type = request.POST.get('component_type')
        component_name = request.POST.get('component_name')
        component_model = request.POST.get('component_model')

        # Create the component
        component_class = get_model_with_component_type(component_type)
        if component_model != "":
            component_class.objects.create(name=component_name, cardModel=component_model)
        else:
            component_class.objects.create(name=component_name)
        return HttpResponseRedirect(reverse('network'))
    else:
        return render(  request, 'network/component_tree/create_component.html', {})


#####################################################################################################
#                     I2C CONNECTIONS
#####################################################################################################
def add_i2c_connection(request, component_type, id):
    # Get the source element
    component_model = get_model_with_component_type(component_type)
    element = get_object_or_404(component_model, pk=id)

    if request.method == 'POST':
        # Retrieve data from user form
        component_type = request.POST.get('component_type')
        component_name = request.POST.get('component_name')
        component_address = request.POST.get('component_address')
        component_model_id = request.POST.get('component_model')

        srcPort = element.i2cPorts.first()
        if srcPort.direction == "DW":
            # Create the target element
            component_class = get_model_with_component_type(component_type)
            if component_model_id is not None:
                component_model_class = get_model_with_component_type(component_type+"Model")
                component_model = component_model_class.objects.get(pk=component_model_id)
                new_component = component_class.objects.create(name=component_name, cardModel=component_model)
            else:
                new_component = component_class.objects.create(name=component_name)
            dstPort = new_component.i2cPorts.create(address=component_address, direction="UP")

            # Link target element to the source element
            srcPort.connection.add(dstPort)
            return HttpResponseRedirect(reverse('network-open', args=[element.component_type(), element.pk]))
        else:
            return HttpResponseBadRequest("I2C port already used.")
    else:
        return render( request, 'network/component_detail/add_i2c_connection.html', {"element": element})

def remove_i2c_connection(request, component_type, component_id, dst_component_type, dst_component_id):
    # Get the source element
    component_model = get_model_with_component_type(component_type)
    element = get_object_or_404(component_model, pk=component_id)

    # Get the destination element
    dst_component_model = get_model_with_component_type(dst_component_type)
    dst_element = get_object_or_404(dst_component_model, pk=dst_component_id)

    # Remove
    dst_element.i2cPorts.all().delete()
    dst_element.delete()
    return HttpResponseRedirect(reverse('network-open', args=[element.component_type(), element.pk]))
