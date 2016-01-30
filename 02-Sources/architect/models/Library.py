"""
    This file include all shared library model
    These data will be updated by the community
"""
from django.db import models


class ArduinoModel(models.Model):
    name = models.CharField("Model Name", max_length=200)
    ioPins = models.IntegerField("Digital I/O Pins", default=0)
    pwmPins = models.IntegerField("PWM Digital I/O Pins", default=0)
    analogIn = models.IntegerField("Analog Input Pins", default=0)

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
