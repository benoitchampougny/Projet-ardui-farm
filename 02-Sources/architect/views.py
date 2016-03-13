"""
  Copyright (c) 2016 Benoit CHAMPOUGNY.  All right reserved.

  This file is part of Arduifarm

  Arduifarm is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  Arduifarm is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
      along with Arduifarm.  If not, see <http://www.gnu.org/licenses/>. 2
"""

from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from architect.models.Network import *
from architect.models.Location import *
from architect.helpers import get_class_by_name
from architect.helpers import get_class_location_by_name

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
            component_class = get_class_by_name(component_type)
            element = get_object_or_404(component_class, pk=component_id)
        return render(  request, 'network/network.html', {'masterElement': masterElement, "element": element})
    else:
        return HttpResponse()

def location(request, component_type=None, component_id=None):
    selectTable = ""
    location = Location.objects.first()
    if location is not None:
        masterElement = location.master
        if component_type is None:
            element = masterElement
        else:
            component_class = get_class_location_by_name(component_type)
            element = get_object_or_404(component_class, pk=component_id)
        return render(  request, 'location/location.html', {'masterElement': masterElement, "element": element, "selectTable": selectTable})
    else:
        return HttpResponse()
#####################################################################################################
#                       COMPONENT DETAILS
#####################################################################################################
def component_detail(request, component_type, component_id):
    component_class = get_class_by_name(component_type)
    element = get_object_or_404(component_class, pk=component_id)
    return render(  request, 'network/component_detail.html', {"element": element})

def location_component_detail(request, component_type, component_id):
    component_class = get_class_location_by_name(component_type)
    element = get_object_or_404(component_class, pk=component_id)
    return render(  request, 'location/component_detail.html', {"element": element})

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
        component_class = get_class_by_name(component_type)
        if component_model != "":
            component_class.objects.create(name=component_name, cardModel=component_model)
        else:
            component_class.objects.create(name=component_name)
        return HttpResponseRedirect(reverse('network'))
    else:
        return render(  request, 'network/component_tree/create_component.html', {})

#####################################################################################################
#                       CREATE LOCATION COMPONENT
#####################################################################################################
def create_location_component(request):
    if request.method == 'POST':
        # Retrieve form parameters
        component_type = request.POST.get('component_type')
        component_name = request.POST.get('component_name')

        # Create the component
        component_class = get_class_by_name(component_type)
        component_class.objects.create(name=component_name)
        return HttpResponseRedirect(reverse('location'))
    else:
        return render(  request, 'location/component_tree/create_component.html', {})
#####################################################################################################
#                     LOCATION CONNECTIONS
#####################################################################################################
def add_location_connection(request, component_type, selectTable, id):
    # Get the source element
    component_model = get_class_location_by_name(component_type)
    element = get_object_or_404(component_model, pk=id)
    if request.method == 'POST':
        # Retrieve data from user form
        component_type = selectTable
        component_name = request.POST.get('component_name')

        srcPort = element.locationPorts.first()

        if srcPort.direction != "DW":
            srcPort = element.locationPorts.create(direction="DW")

        if srcPort.direction == "DW":
            # Create the target element
            component_class = get_class_location_by_name(component_type)
            if selectTable == "Environment" or selectTable == "Zone":
                new_component = component_class.objects.create(name=component_name)
            else:
                new_component = component_name
            dstPort = new_component.locationPorts.create(direction="UP")

            # Link target element to the source element
            srcPort.connection.add(dstPort)
        return HttpResponseRedirect(reverse('location-open', args=[element.component_type(), element.pk]))
    else:
        return render(  request,
                        'location/component_detail/add_location_connection.html',
                        {"element": element, "selectTable": selectTable})

def remove_location_connection(request, component_type, component_id, dst_component_type, dst_component_id):
    # Get the source element
    component_model = get_class_location_by_name(component_type)
    element = get_object_or_404(component_model, pk=component_id)

    # Get the destination element
    dst_component_model = get_class_location_by_name(dst_component_type)
    dst_element = get_object_or_404(dst_component_model, pk=dst_component_id)

    # Remove
    dst_element.locationPorts.all().delete()
    dst_element.delete()
    return HttpResponseRedirect(reverse('location-open',
                                        args=[element.component_type(),
                                              element.pk]))
#####################################################################################################
#                     I2C CONNECTIONS
#####################################################################################################
def add_i2c_connection(request, component_type, id):
    # Get the source element
    component_model = get_class_by_name(component_type)
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
            component_class = get_class_by_name(component_type)
            if component_model_id is not None:
                component_model_class = get_class_by_name(component_type+"Model")
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
        return render(  request,
                        'network/component_detail/add_i2c_connection.html',
                        {"element": element})

def remove_i2c_connection(request, component_type, component_id, dst_component_type, dst_component_id):
    # Get the source element
    component_model = get_class_by_name(component_type)
    element = get_object_or_404(component_model, pk=component_id)

    # Get the destination element
    dst_component_model = get_class_by_name(dst_component_type)
    dst_element = get_object_or_404(dst_component_model, pk=dst_component_id)

    # Remove
    dst_element.i2cPorts.all().delete()
    dst_element.delete()
    return HttpResponseRedirect(reverse('network-open',
                                        args=[element.component_type(),
                                              element.pk]))

#####################################################################################################
#                     DIGITAL CONNECTIONS
#####################################################################################################
def add_dio_connection(request, component_type, id):
    # Get the source element
    component_model = get_class_by_name(component_type)
    element = get_object_or_404(component_model, pk=id)

    if request.method == 'POST':
        # Retrieve data from user form
        remote_component_name = request.POST.get('component_name')
        remote_component_type_name = request.POST.get('component_type')
        remote_component_model_id = request.POST.get('component_model')

        # Retrieve Class from component name
        remote_component_class = get_class_by_name(remote_component_type_name)
        remote_component_model_class = get_class_by_name(remote_component_type_name+"Model")

        # Get the available pin to connect
        element_pins = element.cardModel.pin_set.filter(functions__name="Digital")
        available_pins = element_pins.exclude(ports__in=element.digitalPorts.all())
        sorted_available_pins = sorted(available_pins, key=lambda t: t.priority)

        # Get needed pin
        remote_component_model = remote_component_model_class.objects.get(pk=remote_component_model_id)
        nb_of_digital_pin = remote_component_model.pin_set.filter(functions__name="Digital").count()

        # Connect the pin to the new port
        connected_pins = sorted_available_pins[:nb_of_digital_pin]
        element_new_port = element.digitalPorts.create()
        element_new_port.pins.add(*connected_pins)

        # Create the remote composant
        remote_component = remote_component_class.objects.create(name=remote_component_name,
                                                                 cardModel=remote_component_model)

        # Connect the remote component
        remote_port = remote_component.digitalPorts.create(direction="UP")
        element_new_port.connection.add(remote_port)
        return HttpResponseRedirect(reverse('network-open', args=[element.component_type(), element.pk]))

    else:
        return render(request,
                      'network/component_detail/add_dio_connection.html',
                      {"element": element})

def remove_dio_connection(request, component_type, component_id, dst_component_type, dst_component_id):
    return HttpResponse()


#####################################################################################################
#                       SKETCH GNEERATION
#####################################################################################################
def generate_sketch(request, arduino_id):
    arduino = get_object_or_404(Arduino, pk=arduino_id)
    response = render(request,
                      'sketches/arduino.ino',
                      {"element": arduino})
    response['Content-Disposition'] = 'attachment; filename=arduino.ino'
    return response
