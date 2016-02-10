"""
    This file include all shared library model
    These data will be updated by the community
"""
from django.db import models
from django.db.models import Max


class ArduinoModel(models.Model):
    name = models.CharField("Model Name", max_length=200)

    def __unicode__(self):
        return self.name


class Pin(models.Model):
    number = models.IntegerField(default=0)
    arduino = models.ForeignKey('ArduinoModel')
    functions = models.ManyToManyField('PinFunction')

    class Meta:
        ordering = ['number']

    def __unicode__(self):
        name = "%s-%02d" % (self.arduino.name, self.number)
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
    sketch = models.FileField(upload_to='sketches/', null=True, default=None)

    def __unicode__(self):
        return self.name


class ActuatorModel(models.Model):
    name = models.CharField("Model Name", max_length=200)
    sketch = models.FileField(upload_to='sketches/', null=True, default=None)

    def __unicode__(self):
        return self.name
