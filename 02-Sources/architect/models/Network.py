"""
    This file will contain models that are related to
    - the network architecture,
    - the interconnection between elements (interfaces)
"""
from django.db import models


class Network(models.Model):
    name = models.CharField("Network Name", max_length=200)
    master = models.ForeignKey('Raspberry', null=True, default=None, blank=True)

    def __unicode__(self):
        return self.name


class ArduinoModel(models.Model):
    name = models.CharField("Model Name", max_length=200)
    ioPins = models.IntegerField("Digital I/O Pins", default=0)
    pwmPins = models.IntegerField("PWM Digital I/O Pins", default=0)
    analogIn = models.IntegerField("Analog Input Pins", default=0)

    def __unicode__(self):
        return self.name


class Arduino(models.Model):
    name = models.CharField("Card Name", max_length=200)
    cardModel = models.ForeignKey('ArduinoModel', null=True, default=None, blank=True)

    def __unicode__(self):
        return self.name


class RaspberryModel(models.Model):
    name = models.CharField("Model Name", max_length=200)

    def __unicode__(self):
        return self.name


class Raspberry(models.Model):
    name = models.CharField("Card Name", max_length=200)
    cardModel = models.ForeignKey('RaspberryModel', null=True, default=None, blank=True)

    def __unicode__(self):
        return self.name


class SensorModel(models.Model):
    name = models.CharField("Model Name", max_length=200)
    sketch = models.FileField(upload_to='sketches/', null=True, default=None)

    def __unicode__(self):
        return self.name


class Sensor(models.Model):
    name = models.CharField("Card Name", max_length=200)
    cardModel = models.ForeignKey('SensorModel', null=True, default=None, blank=True)

    def __unicode__(self):
        return self.name

class Port(models.Model):
    number = models.IntegerField(default=1)
    interfaceType = models.ForeignKey("InterfaceType", null=True, default=None, blank=True)

    def __unicode__(self):
        return self.name

class InterfaceType(models.Model):
    name = models.CharField("Interface Type Name", max_length=200)

    def __unicode__(self):
        return self.name

class Connection(models.Model):
    source = models.ForeignKey("Port", null=True, default=None, blank=True, related_name="target")
    target = models.ForeignKey("Port", null=True, default=None, blank=True, related_name="source")
