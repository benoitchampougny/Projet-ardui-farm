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
    version = models.FloatField('Version', default=0.0)

    def __unicode__(self):
        return self.name

class ActuatorModel(models.Model):
    name = models.CharField("Model Name", max_length=200)
    brand = models.CharField("Brand", max_length=200)
    version = models.FloatField('Version', default=0.0)
    lastVersion = models.BooleanField('Last Version', default=True)
    sketch = models.FileField(upload_to='sketches/', blank=True, null=True)

    def __unicode__(self):
        return self.name

class ActuatedModel(models.Model):
    name = models.CharField("Model Name", max_length=200)
    brand = models.CharField("Brand", max_length=200)
    element = models.ForeignKey('Element', null=True, default=None, blank=True)
    version = models.FloatField('Version', default=0.0)
    flowActuator = models.BooleanField('Flow Actuator', default=False)
    lastVersion = models.BooleanField('Last Version', default=True)

    def __unicode__(self):
        return self.name

class Boolean(models.Model):
    name = models.CharField('Boolean Name', max_length=200)
    version = models.FloatField('Version', default=0.0)
    lastVersion = models.BooleanField('Last Version', default=True)
    true = models.CharField('True', max_length=200)
    false = models.CharField('False', max_length=200)
    element = models.ManyToManyField('Element',  blank=True)

    def __unicode__(self):
        return self.name

class Element(models.Model):
    name = models.CharField('Element Name', max_length=200)
    version = models.FloatField('Version', default=0.0)
    lastVersion = models.BooleanField('Last Version', default=True)

    def __unicode__(self):
        return self.name

class OptionalFunctionModel(models.Model):
    name = models.CharField('Function Name', max_length=200)
    version = models.FloatField('Version', default=0.0)
    lastVersion = models.BooleanField('Last Version', default=True)
    pinfunction = models.ManyToManyField('PinFunction', blank=True)
    priority = models.IntegerField('Function Priority', default=0)

    def __unicode__(self):
        return self.name


class GroupFunctionModel(models.Model):
    name = models.CharField('Function Name', max_length=200)
    version = models.FloatField('Version', default=0.0)
    lastVersion = models.BooleanField('Last Version', default=True)
    pinfunction = models.ManyToManyField('PinFunction', blank=True)
    priority = models.IntegerField('Function Priority', default=0)
    optionalFunctionModel = models.ForeignKey('OptionalFunctionModel', null=True, default=None, blank=True)

    @property
    def parent(self):
        if self.optionalFunctionModel is not None:
            return self.optionalFunctionModel

    def __unicode__(self):
        return self.name

class I2cAdress(models.Model):
    name = models.CharField("I2c Adress Name", max_length=200)

    def __unicode__(self):
        return self.name


class InfluenceMeasure(models.Model):
    measure = models.ForeignKey('Measure', null=True, default=None, blank=True)
    actuated = models.ForeignKey('ActuatedModel', null=True, default=None, blank=True)
    direction = models.CharField('Direction', max_length=200)

    def __unicode__(self):
        name = "%s - [%s] [%s]" % (self.actuated, self.measure, self.direction)
        return name

class Measure(models.Model):
    name = models.CharField('Measure Name', max_length=200)
    version = models.FloatField('Version', default=0.0)
    lastVersion = models.BooleanField('Last Version', default=True)
    unit = models.ManyToManyField('Unit', blank=True)

    def __unicode__(self):
        return self.name

class OptionalFunction(models.Model):
    name = models.CharField('Function Name', max_length=200)
    version = models.FloatField('Version', default=0.0)
    lastVersion = models.BooleanField('Last Version', default=True)
    optionalPin = models.ForeignKey('PinFunction', max_length=200)
    priority = models.IntegerField('Function Priority', default=0)

    def __unicode__(self):
        return self.name

class PinShield(models.Model):
    number = models.CharField(max_length=200)
    actuator = models.ForeignKey('ActuatorModel', null=True, default=None, blank=True)
    sensor = models.ForeignKey('SensorModel', null=True, default=None, blank=True)
    arduino = models.ForeignKey('ArduinoModel', null=True, default=None, blank=True)
    raspberry = models.ForeignKey('RaspberryModel', null=True, default=None, blank=True)
    shield = models.ForeignKey('ShieldModel', null=True, default=None, blank=True)

    class Meta:
        ordering = ['number']

    @property
    def parent(self):
        if self.raspberry is not None:
            return self.raspberry
        if self.arduino is not None:
            return self.arduino

    @property
    def children(self):
        if self.sensor is not None:
            return self.sensor
        if self.actuator is not None:
            return self.actuator

    def __unicode__(self):
        name = "%s - [%s] [%s] [pin-%s]" % (self.shield, self.parent.name, self.children.name, self.number)
        return name

    @property
    def priority(self):
        return self.functions.all().aggregate(Sum('priority'))

class PinGroup(models.Model):
    number = models.CharField(max_length=200)
    groupFunctionModel = models.ForeignKey('GroupFunctionModel', null=True, default=None, blank=True)
    pin = models.ManyToManyField('Pin', blank=True)
    actuator = models.ForeignKey('ActuatorModel', null=True, default=None, blank=True)
    sensor = models.ForeignKey('SensorModel', null=True, default=None, blank=True)
    arduino = models.ForeignKey('ArduinoModel', null=True, default=None, blank=True)
    raspberry = models.ForeignKey('RaspberryModel', null=True, default=None, blank=True)

    class Meta:
        ordering = ['number']


    @property
    def parent(self):
        if self.raspberry is not None:
            return self.raspberry
        if self.arduino is not None:
            return self.arduino
        if self.sensor is not None:
            return self.sensor
        if self.actuator is not None:
            return self.actuator

    def __unicode__(self):
        name = "[%s] [%s] [%s]" % (self.parent.name, self.number, self.groupFunctionModel.name)
        return name

    @property
    def priority(self):
        return self.functions.all().aggregate(Sum('priority'))


class Pin(models.Model):
    number = models.CharField(max_length=200)
    functions = models.ManyToManyField('PinFunction')
    actuator = models.ForeignKey('ActuatorModel', null=True, default=None, blank=True)
    sensor = models.ForeignKey('SensorModel', null=True, default=None, blank=True)
    arduino = models.ForeignKey('ArduinoModel', null=True, default=None, blank=True)
    raspberry = models.ForeignKey('RaspberryModel', null=True, default=None, blank=True)

    class Meta:
        ordering = ['number']

    @property
    def parent(self):
        if self.raspberry is not None:
            return self.raspberry
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

class PinFunction(models.Model):
    name = models.CharField('Function Name', max_length=200)
    version = models.FloatField('Version', default=0.0)
    lastVersion = models.BooleanField('Last Version', default=True)
    detail = models.CharField('detail', null=True, default=None, max_length=200)
    priority = models.IntegerField('Function Priority', default=0)

    def __unicode__(self):
        return self.name

class RaspberryModel(models.Model):
    name = models.CharField("Model Name", max_length=200)
    version = models.FloatField('Version', default=0.0)
    lastVersion = models.BooleanField('Last Version', default=True)

    def __unicode__(self):
        return self.name

class SensorModel(models.Model):
    name = models.CharField("Model Name", max_length=200)
    version = models.FloatField('Version', default=0.0)
    lastVersion = models.BooleanField('Last Version', default=True)
    sketch = models.FileField(upload_to='sketches/', blank=True, null=True)
    i2cAdress = models.ManyToManyField('i2cAdress',  blank=True)
    measure = models.ManyToManyField('Measure',  blank=True)
    element = models.ForeignKey('Element', null=True, default=None, blank=True)
    boolean = models.ForeignKey('Boolean', null=True, default=None, blank=True)

    def __unicode__(self):
        return self.name

class SpecialMeasure(models.Model):
    name = models.CharField('Special Measure Name', max_length=200)
    version = models.FloatField('Version', default=0.0)
    lastVersion = models.BooleanField('Last Version', default=True)
    specialUnity = models.CharField('Special Unity', max_length=200)

    def __unicode__(self):
        return self.name


class ShieldModel(models.Model):
    name = models.CharField("Model Name", max_length=200)
    version = models.FloatField('Version', default=0.0)
    lastVersion = models.BooleanField('Last Version', default=True)

    def __unicode__(self):
        return self.name

class TechnicalCaracteristic(models.Model):
    value =  models.FloatField('Value', default=0.0)
    measure = models.ForeignKey('Measure', null=True, default=None, blank=True)
    unit = models.ForeignKey('Unit', null=True, default=None, blank=True)
    actuated = models.ForeignKey('ActuatedModel', null=True, default=None, blank=True)


    class Meta:
        ordering = ['actuated']

    def __unicode__(self):
        name = "%s - [%s: %s %s]" % (self.actuated, self.measure, self.value, self.unit)
        return name

class Unit(models.Model):
    name = models.CharField('Unit Name', max_length=200)
    shortUnit = models.CharField('Short Unit', max_length=200)

    def __unicode__(self):
        return self.name

class Update(models.Model):
    name = models.CharField('Name Update', max_length=200)
    version = models.FloatField('Version', default=0.0)
    date = models.DateTimeField (auto_now_add=True)


    class Meta:
        ordering = ['date']

    def __unicode__(self):
        name = "update %s version %d date %s-%s-%s" % (self.name, self.version, self.date.day, self.date.month, self.date.year)
        return name
