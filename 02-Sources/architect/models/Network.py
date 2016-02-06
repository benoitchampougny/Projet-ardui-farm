"""
    This file will contain models that are related to
    - the network architecture,
    - the interconnection between elements (interfaces)
"""
from django.db import models
from architect.models.Library import *


class Network(models.Model):
    name = models.CharField("Network Name", max_length=200)
    master = models.ForeignKey('Raspberry', null=True, default=None, blank=True)

    def __unicode__(self):
        return self.name


class NetworkComponent:
    """ Class to define common interface between components """
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

    def downI2C(self):
        return self.i2cPorts.filter(direction="DW")

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


class Actuator(models.Model, NetworkComponent):
    name = models.CharField("Card Name", max_length=200)
    cardModel = models.ForeignKey('ActuatorModel', null=True, default=None, blank=True)


class I2cPort(models.Model):
    DIRECTIONS = (
        ("UP", "Upward"),
        ("DW", "Downward"),
    )
    direction = models.CharField(max_length=2, choices=DIRECTIONS, default="DW")
    address = models.CharField("I2C Address", max_length=200, default=None, blank=True)
    connection = models.ManyToManyField("self", blank=True)

    def __unicode__(self):
        if self.parent is not None:
            return "%s-%s" % (self.parent.name, self.address)
        return self.address

    @property
    def parent(self):
        if self.arduino_set.count() > 0:
            return self.arduino_set.first()
        elif self.raspberry_set.count() > 0:
            return self.raspberry_set.first()


class WifiPort(models.Model):
    number = models.IntegerField("Number", default=1)
    address = models.CharField("IP Address", max_length=200, default=None, blank=True)
    port = models.IntegerField("UDP Port", default=8000, blank=True)
    password = models.CharField("Password", max_length=200, default=None, blank=True)
    connection = models.ManyToManyField("self", blank=True)

    def __unicode__(self):
        return self.address

    @property
    def parent(self):
        if self.arduino_set.count() > 0:
            return self.arduino_set.first()
        elif self.raspberry_set.count() > 0:
            return self.raspberry_set.first()
