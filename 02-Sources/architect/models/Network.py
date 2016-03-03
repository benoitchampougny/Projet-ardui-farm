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

class Network(models.Model):
    name = models.CharField("Network Name", max_length=200)
    master = models.ForeignKey('Raspberry', null=True, default=None, blank=True)

    def __unicode__(self):
        return self.name

class NetworkComponent:
    """ Class to define common methods between components """
    def __unicode__(self):
        return self.name

    def _get_component_name(self):
        return self.__class__.__name__

    def tree_element_template(self):
        component = self._get_component_name()
        return "network/%s/tree_element.html" % component

    def detail_element_template(self):
        component = self._get_component_name()
        return "network/%s/element_details.html" % component

    def component_type(self):
        return self._get_component_name()


class Arduino(models.Model, NetworkComponent):
    name = models.CharField("Card Name", max_length=200)
    cardModel = models.ForeignKey('ArduinoModel', null=True, default=None, blank=True)
    i2cPorts = models.ManyToManyField("I2cPort", blank=True)
    digitalPorts = models.ManyToManyField("DigitalPort", blank=True)


    def downI2C(self):
        return self.i2cPorts.filter(direction="DW")

    def downDIO(self):
        return self.digitalPorts.filter(direction="DW")

    def initDigitalPorts(self):
        for pin in self.cardModel.pin_set.filter(functions__name="digital"):
            dio = DigitalPort.objects.create(pin=pin)
            self.digitalPorts.add(dio)


class Raspberry(models.Model, NetworkComponent):
    name = models.CharField("Card Name", max_length=200)
    cardModel = models.ForeignKey('RaspberryModel', null=True, default=None, blank=True)
    i2cPorts = models.ManyToManyField("I2cPort", blank=True)
    wifiPorts = models.ManyToManyField("WifiPort", blank=True)

    def downI2C(self):
        return self.i2cPorts.filter(direction="DW")


class Sensor(models.Model, NetworkComponent):
    name = models.CharField("Card Name", max_length=200)
    cardModel = models.ForeignKey('SensorModel', null=True, default=None, blank=True)
    digitalPorts = models.ManyToManyField("DigitalPort", blank=True)
    LocationPorts = models.ManyToManyField("LocationPort", blank=True)

    def downDIO(self):
        return self.digitalPorts.filter(direction="DW")

    def downLocation(self):
        return self.locationPorts.filter(direction="DW")

class Actuator(models.Model, NetworkComponent):
    name = models.CharField("Card Name", max_length=200)
    cardModel = models.ForeignKey('ActuatorModel', null=True, default=None, blank=True)
    digitalPorts = models.ManyToManyField("DigitalPort", blank=True)
    LocationPorts = models.ManyToManyField("LocationPort", blank=True)

    def downDIO(self):
        return self.digitalPorts.filter(direction="DW")

    def downLocation(self):
        return self.locationPorts.filter(direction="DW")

class GenericPort(models.Model):
    DIRECTIONS = (
        ("UP", "Upward"),
        ("DW", "Downward"),
    )
    direction = models.CharField(max_length=2, choices=DIRECTIONS, default="DW")
    address = models.CharField("Address", max_length=200, default=None, blank=True, null=True)
    connection = models.ManyToManyField("self", blank=True)

    class Meta:
        # Only use for inheritance.
        abstract = True

    def __unicode__(self):
        if self.parent is not None:
            return "%s-%s" % (self.parent.name, self.address)
        return self.address

    def _get_parent(self, parentNames):
        for parentName in parentNames:
            parentRelation = getattr(self, parentName+"_set")
            if parentRelation.count() > 0:
                return parentRelation.first()


class I2cPort(GenericPort):
    @property
    def parent(self):
        return self._get_parent(['arduino', 'raspberry'])


class DigitalPort(GenericPort):
    pins = models.ManyToManyField('Pin', related_name="ports")
    @property
    def parent(self):
        return self._get_parent(['arduino', 'sensor', 'actuator'])


class WifiPort(GenericPort):
    port = models.IntegerField("UDP Port", default=8000, blank=True)
    password = models.CharField("Password", max_length=200, default=None, blank=True)

    @property
    def parent(self):
        return self._get_parent(['arduino', 'raspberry'])
