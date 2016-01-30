from django.shortcuts import render
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
