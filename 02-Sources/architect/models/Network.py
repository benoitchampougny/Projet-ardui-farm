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
    digitalPorts = models.ManyToManyField("DigitalPort", blank=True)

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
    digitalPorts = models.ManyToManyField("DigitalPort", blank=True)


class Actuator(models.Model, NetworkComponent):
    name = models.CharField("Card Name", max_length=200)
    cardModel = models.ForeignKey('ActuatorModel', null=True, default=None, blank=True)


class GenericPort(models.Model):
    DIRECTIONS = (
        ("UP", "Upward"),
        ("DW", "Downward"),
    )
    direction = models.CharField(max_length=2, choices=DIRECTIONS, default="DW")
    address = models.CharField("Address", max_length=200, default=None, blank=True)
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
    pwm = models.BooleanField(default=False)
    @property
    def parent(self):
        return self._get_parent(['arduino', 'sensor', 'actuator'])


class WifiPort(GenericPort):
    port = models.IntegerField("UDP Port", default=8000, blank=True)
    password = models.CharField("Password", max_length=200, default=None, blank=True)

    @property
    def parent(self):
        return self._get_parent(['arduino', 'raspberry'])
