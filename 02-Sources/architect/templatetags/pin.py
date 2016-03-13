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
from django import template
from architect.models import Network, Library

register = template.Library()

@register.assignment_tag(takes_context=True)
def get_arduino_pin(context, function_name, pin_number=""):
    connected_port = context['connected_port']
    pins = connected_port.pins.filter(functions__name = function_name)
    if len(pins) > 1:
        pin = pins.get(number=pin_number)
    else:
        pin = pins.first()
    return pin
