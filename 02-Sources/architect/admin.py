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

from django.contrib import admin
from architect.models import Location, Network, Library, Message
# Register your models here.


# Location package
admin.site.register(Location.Location)
admin.site.register(Location.Environment)
admin.site.register(Location.Zone)
admin.site.register(Location.LocationPort)
admin.site.register(Location.Scenario)


# Network package
admin.site.register(Network.Network)
admin.site.register(Network.Arduino)
admin.site.register(Network.Raspberry)
admin.site.register(Network.Sensor)
admin.site.register(Network.I2cPort)
admin.site.register(Network.DigitalPort)
admin.site.register(Network.WifiPort)
admin.site.register(Network.Actuator)

# Library package
admin.site.register(Library.RaspberryModel)
admin.site.register(Library.ArduinoModel)
admin.site.register(Library.SensorModel)
admin.site.register(Library.ActuatorModel)
admin.site.register(Library.Pin)
admin.site.register(Library.PinFunction)
admin.site.register(Library.ShieldModel)
admin.site.register(Library.I2cAdress)
admin.site.register(Library.Element)
admin.site.register(Library.Boolean)
admin.site.register(Library.SpecialMeasure)
admin.site.register(Library.Measure)
admin.site.register(Library.OptionalFunction)
admin.site.register(Library.GroupFunction)
admin.site.register(Library.Unit)
admin.site.register(Library.OptionalFunctionModel)
admin.site.register(Library.GroupFunctionModel)

# Message
admin.site.register(Message.Message)
admin.site.register(Message.BCDData)
