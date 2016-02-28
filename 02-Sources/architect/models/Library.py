"""
    This file include all shared library model
    These data will be updated by the community
"""
from django.db import models
from django.db.models import Sum


class ArduinoModel(models.Model):
    name = models.CharField("Model Name", max_length=200)

    def __unicode__(self):
        return self.name


class Pin(models.Model):
    number = models.IntegerField(default=0)
    functions = models.ManyToManyField('PinFunction')
    actuator = models.ForeignKey('ActuatorModel', null=True, default=None, blank=True)
    sensor = models.ForeignKey('SensorModel', null=True, default=None, blank=True)
    arduino = models.ForeignKey('ArduinoModel', null=True, default=None, blank=True)

    class Meta:
        ordering = ['number']

    @property
    def parent(self):
        if self.arduino is not None:
            return self.arduino
        if self.sensor is not None:
            return self.sensor
        if self.actuator is not None:
            return self.actuator

    def __unicode__(self):
        name = "%s-%02d" % (self.parent.name, self.number)
        for function in self.functions.all():
            name += " [%s]" % function.name
        return name

    @property
    def priority(self):
        return self.functions.all().aggregate(Sum('priority'))


class PinFunction(models.Model):
    name = models.CharField('Function Name', max_length=200)
    priority = models.IntegerField('Function Priority', default=0)

    def __unicode__(self):
        return self.name

class RaspberryModel(models.Model):
    name = models.CharField("Model Name", max_length=200)

    def __unicode__(self):
        return self.name


class SensorModel(models.Model):
    name = models.CharField("Model Name", max_length=200)
    sketch = models.FileField(upload_to='sketches/', blank=True, null=True)
    def __unicode__(self):
        return self.name


class ActuatorModel(models.Model):
    name = models.CharField("Model Name", max_length=200)
    sketch = models.FileField(upload_to='sketches/', blank=True, null=True)

    def __unicode__(self):
        return self.name
