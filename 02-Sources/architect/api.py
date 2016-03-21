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

from django.http import JsonResponse
from django.core import serializers
from architect.helpers import get_class_by_name

def get_component_model(request):
    component_type = request.GET.get('component_type')
    component_class = get_class_by_name(component_type + "Model")
    values = component_class.objects.all()
    return JsonResponse(serializers.serialize('json', values), safe=False)
