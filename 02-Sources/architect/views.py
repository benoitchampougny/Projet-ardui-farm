from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

def home(request):
    return HttpResponseRedirect(reverse('network'))

def network(request):
    return render(  request, 'network/network.html')
