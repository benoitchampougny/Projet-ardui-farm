from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from architect.models.Network import *


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
            Component = ComponentModel[component_type]
            element = get_object_or_404(Component, pk=component_id)
        return render(  request, 'network/network.html', {'masterElement': masterElement, "element": element})
    else:
        return HttpResponse()


#####################################################################################################
#                       COMPONENT DETAILS
#####################################################################################################
def component_detail(request, component_type, component_id):
    detail_view_url = reverse('network-%s-detail' % component_type, args=[component_id])
    return HttpResponseRedirect(detail_view_url)

def detail_arduino(request, id):
    element = get_object_or_404(Arduino, pk=id)
    return render(  request, 'network/component_detail.html', {"element": element})
def detail_raspberry(request, id):
    element = get_object_or_404(Raspberry, pk=id)
    return render(  request, 'network/component_detail.html', {"element": element})
def detail_sensor(request, id):
    element = get_object_or_404(Sensor, pk=id)
    return render(  request, 'network/component_detail.html', {})
def detail_actuator(request, id):
    element = get_object_or_404(Actuator, pk=id)
    return render(  request, 'network/component_detail.html', {})


#####################################################################################################
#                       CREATE COMPONENT
#####################################################################################################
def create_component_helper(component_type, component_name):
    if component_type == "Arduino":
        component = Arduino.objects.create(name=component_name)
    elif component_type == "Raspberry":
        component = Raspberry.objects.create(name=component_name)
    elif component_type == "Sensor":
        component = Sensor.objects.create(name=component_name)
    elif component_type == "Actuator":
        component = Actuator.objects.create(name=component_name)
    return component


def create_component(request):
    if request.method == 'POST':
        component_type = request.POST.get('component_type')
        component_name = request.POST.get('component_name')
        create_component_helper(component_type, component_name)
        return HttpResponseRedirect(reverse('network'))
    else:
        return render(  request, 'network/component_tree/create_component.html', {})


#####################################################################################################
#                      CONNECTIONS
#####################################################################################################
def add_i2c_connection(request, component_type, id):
    # Get the source element
    if component_type == "raspberry":
        element = get_object_or_404(Raspberry, pk=id)
    elif component_type == "arduino":
        element = get_object_or_404(Arduino, pk=id)

    if request.method == 'POST':
        # Create the target element
        component_type = request.POST.get('component_type')
        component_name = request.POST.get('component_name')
        component_address = request.POST.get('component_address')

        srcPort = element.i2cPorts.first()
        if srcPort.direction == "DW":
            new_component = create_component_helper(component_type, component_name)
            dstPort = new_component.i2cPorts.create(address=component_address, direction="UP")
            srcPort.connection.add(dstPort)
            return HttpResponseRedirect(reverse('network-open', args=[element.component_type(), element.pk]))
        else:
            return HttpResponseBadRequest("I2C port already used.")
    else:
        return render( request, 'network/component_detail/add_i2c_connection.html', {"element": element})
