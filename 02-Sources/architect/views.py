from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from architect.models.Network import *

def home(request):
    return HttpResponseRedirect(reverse('network'))

def network(request):
    network = Network.objects.first()
    if network is not None:
        masterElement = network.master
        return render(  request, 'network/network.html', {'masterElement': masterElement})
    else:
        return HttpResponse()

def component_detail(request, component_type, component_id):
    detail_view_url = reverse('network-%s-detail' % component_type, args=[component_id])
    return HttpResponseRedirect(detail_view_url)

def detail_arduino(request, id):
    element = get_object_or_404(Arduino, pk=id)
    return render(  request, 'network/component_detail.html', {"element":element})
def detail_raspberry(request, id):
    element = get_object_or_404(Raspberry, pk=id)
    return render(  request, 'network/component_detail.html', {"element":element})
def detail_sensor(request, id):
    element = get_object_or_404(Sensor, pk=id)
    return render(  request, 'network/component_detail.html', {})
def detail_actuator(request, id):
    element = get_object_or_404(Actuator, pk=id)
    return render(  request, 'network/component_detail.html', {})
