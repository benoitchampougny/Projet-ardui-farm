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
"""
    This file will contain models that are related to
    - the network architecture,
    - the interconnection between elements (interfaces)
"""
from django.db import models
from architect.models.Library import *
from architect.models.Location import *
from architect.models.Message import *

class Network(models.Model):
    name = models.CharField("Network Name", max_length=200)
    master = models.ForeignKey('Raspberry', null=True, default=None, blank=True)

    def __unicode__(self):
        return self.name


class NetworkComponent(models.Model):
    i2cConnection = models.ForeignKey('self', related_name='i2cSubComponent', null=True, default=None, blank=True)
    wifiConnection = models.ForeignKey('self', related_name='wifiSubComponent', null=True, default=None, blank=True)
    dioConnection = models.ForeignKey('self', related_name='dioSubComponent', null=True, default=None, blank=True)

    @property
    def type(self):
        for typeName in ["raspberry", "arduino", "sensor", "actuator"]:
            if hasattr(self, typeName):
                return getattr(self, typeName)

    def __unicode__(self):
        return self.type.name


class Arduino(NetworkComponent):
    name = models.CharField("Card Name", max_length=200)
    cardModel = models.ForeignKey('ArduinoModel', null=True, default=None, blank=True)

    def __unicode__(self):
        return self.name


class Raspberry(NetworkComponent):
    name = models.CharField("Card Name", max_length=200)
    cardModel = models.ForeignKey('RaspberryModel', null=True, default=None, blank=True)

    def __unicode__(self):
        return self.name

class Sensor(NetworkComponent):
    name = models.CharField("Card Name", max_length=200)
    cardModel = models.ForeignKey('SensorModel', null=True, default=None, blank=True)
    LocationPorts = models.ManyToManyField("LocationPort", blank=True)

    def __unicode__(self):
        return self.name

    def downLocation(self):
        return self.locationPorts.filter(direction="DW")

class Actuator(NetworkComponent):
    name = models.CharField("Card Name", max_length=200)
    cardModel = models.ForeignKey('ActuatorModel', null=True, default=None, blank=True)
    LocationPorts = models.ManyToManyField("LocationPort", blank=True)

    def downLocation(self):
        return self.locationPorts.filter(direction="DW")


class Port(models.Model):
    component = models.ForeignKey('NetworkComponent')
    pin = models.ForeignKey('Pin', related_name="ports")
    connection = models.ManyToManyField('Port')
