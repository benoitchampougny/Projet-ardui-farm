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
  along with Arduifarm.  If not, see <http://www.gnu.org/licenses/>.
"""

"""
    This file include all shared library model
    These data will be updated by the community
"""
from django.db import models
from django.db.models import Sum


class ArduinoModel(models.Model):
    name = models.CharField("Model Name", max_length=200)
    version = models.CharField('Version', null=True, default=None, max_length=200)

    def __unicode__(self):
        return self.name

class ShieldModel(models.Model):
    name = models.CharField("Model Name", max_length=200)
    version = models.CharField('Version', null=True, default=None, max_length=200)

    def __unicode__(self):
        return self.name

class I2cAdress(models.Model):
    name = models.CharField("I2c Adress Name", max_length=200)
    actuator = models.ForeignKey('ActuatorModel', null=True, default=None, blank=True)
    sensor = models.ForeignKey('SensorModel', null=True, default=None, blank=True)

    def __unicode__(self):
        return self.name

class Pin(models.Model):
    number = models.CharField(max_length=100)
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
        name = "%s-%s" % (self.parent.name, self.number)
        for function in self.functions.all():
            name += " [%s]" % function.name
        return name

    @property
    def priority(self):
        return self.functions.all().aggregate(Sum('priority'))

class Element(models.Model):
    name = models.CharField('Element Name', max_length=200)
    version = models.CharField('Version', null=True, default=None, max_length=200)
    actuator = models.ForeignKey('ActuatorModel', null=True, default=None, blank=True)
    sensor = models.ForeignKey('SensorModel', null=True, default=None, blank=True)

    def __unicode__(self):
        return self.name

class Boolean(models.Model):
    name = models.CharField('Boolean Name', max_length=200)
    version = models.CharField('Version', null=True, default=None, max_length=200)
    element = models.ForeignKey('Element', max_length=200)
    true = models.CharField('True', max_length=200)
    false = models.CharField('False', max_length=200)
    actuator = models.ForeignKey('ActuatorModel', null=True, default=None, blank=True)
    sensor = models.ForeignKey('SensorModel', null=True, default=None, blank=True)

    def __unicode__(self):
        return self.name

class SpecialMeasure(models.Model):
    name = models.CharField('Special Measure Name', max_length=200)
    version = models.CharField('Version', null=True, default=None, max_length=200)
    specialUnity = models.CharField('Special Unity', max_length=200)

    def __unicode__(self):
        return self.name

class Measure(models.Model):
    name = models.CharField('Measure Name', max_length=200)
    version = models.CharField('Version', null=True, default=None, max_length=200)
    nameUnity = models.CharField('Unity Of Measue', max_length=200)
    actuator = models.ForeignKey('ActuatorModel', null=True, default=None, blank=True)
    sensor = models.ForeignKey('SensorModel', null=True, default=None, blank=True)

    def __unicode__(self):
        return self.name

class PinFunction(models.Model):
    name = models.CharField('Function Name', max_length=200)
    version = models.CharField('Version', null=True, default=None, max_length=200)
    shortName = models.CharField('Function Short Name', null=True, default=None, max_length=200)
    priority = models.IntegerField('Function Priority', default=0)

    def __unicode__(self):
        return self.name

class OptionalFunction(models.Model):
    name = models.CharField('Function Name', max_length=200)
    version = models.CharField('Version', null=True, default=None, max_length=200)
    optionalPin = models.ForeignKey('PinFunction', max_length=200)
    priority = models.IntegerField('Function Priority', default=0)

    def __unicode__(self):
        return self.name


class GroupFunction(models.Model):
    name = models.CharField('Function Name', max_length=200)
    version = models.CharField('Version', null=True, default=None, max_length=200)
    groupPin = models.ForeignKey('PinFunction', null=True, default=None, max_length=200)
    optionalPin = models.ForeignKey('OptionalFunction', null=True, default=None, max_length=200)
    priority = models.IntegerField('Function Priority', default=0)

    def __unicode__(self):
        return self.name


class RaspberryModel(models.Model):
    name = models.CharField("Model Name", max_length=200)
    version = models.CharField("Version", null=True, default=None, max_length=200)

    def __unicode__(self):
        return self.name


class SensorModel(models.Model):
    name = models.CharField("Model Name", max_length=200)
    version = models.CharField("Version", null=True, default=None, max_length=200)
    publish = models.ManyToManyField('Message', blank=True)

    def __unicode__(self):
        return self.name


class ActuatorModel(models.Model):
    name = models.CharField("Model Name", max_length=200)
    version = models.CharField("Version", null=True, default=None, max_length=200)
    sketch = models.FileField(upload_to='sketches/', blank=True, null=True)
    suscribe = models.ManyToManyField('Message', blank=True)

    def __unicode__(self):
        return self.name
