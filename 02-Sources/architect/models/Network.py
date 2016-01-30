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


class Arduino(models.Model):
    name = models.CharField("Card Name", max_length=200)
    cardModel = models.ForeignKey('ArduinoModel', null=True, default=None, blank=True)
    i2cPorts = models.ManyToManyField("I2cPort", default=None, blank=True)

    def __unicode__(self):
        return self.name

    def tree_element_template(self):
        return "network/arduino/tree_element.html"

class Raspberry(models.Model):
    name = models.CharField("Card Name", max_length=200)
    cardModel = models.ForeignKey('RaspberryModel', null=True, default=None, blank=True)
    i2cPorts = models.ManyToManyField("I2cPort", default=None, blank=True)
    wifiPorts = models.ManyToManyField("WifiPort", default=None, blank=True)

    def __unicode__(self):
        return self.name

    def tree_element_template(self):
        return "network/raspberry/tree_element.html"


class Sensor(models.Model):
    name = models.CharField("Card Name", max_length=200)
    cardModel = models.ForeignKey('SensorModel', null=True, default=None, blank=True)

    def __unicode__(self):
        return self.name

    def tree_element_template(self):
        return "networl/sensor/tree_element"

class Actuator(models.Model):
    name = models.CharField("Card Name", max_length=200)
    cardModel = models.ForeignKey('ActuatorModel', null=True, default=None, blank=True)

    def __unicode__(self):
        return self.name


class I2cPort(models.Model):
    number = models.IntegerField("Number", default=1)
    address = models.CharField("I2C Address", max_length=200, default=None, blank=True)
    connection = models.ManyToManyField("self", default=None, blank=True)

    def __unicode__(self):
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
    connection = models.ManyToManyField("self", default=None, blank=True)

    def __unicode__(self):
        return self.address

    @property
    def parent(self):
        if self.arduino_set.count() > 0:
            return self.arduino_set.first()
        elif self.raspberry_set.count() > 0:
            return self.raspberry_set.first()
