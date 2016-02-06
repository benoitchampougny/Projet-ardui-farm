from django.http import JsonResponse
from django.core import serializers
from architect.helpers import get_model_with_component_type

def get_component_model(request):
    component_type = request.GET.get('component_type')
    component_class = get_model_with_component_type(component_type + "Model")
    values = component_class.objects.all()
    return JsonResponse(serializers.serialize('json', values), safe=False)
