"""
    This file will contain models that are related to
    - space, area, room, etc
        To define where network element is located
    - The sementic name of a measure or of an element for example Temperature, Engine, etc
"""
from django.db import models
from architect.models.Network import Sensor

class Location(models.Model):
    name = models.CharField("Location Name", max_length=200)
    inside = models.ForeignKey("Location", related_name="contain")
    def __unicode__(self):
        return self.name


class TechnicalElement(models.Model):
    name = models.CharField("Technical Element Name", max_length=200)
    location = models.ForeignKey("Location", null=True, default=None, blank=True)

    def __unicode__(self):
        return self.name


class Measure(models.Model):
    name = models.CharField("Measure Name", max_length=200)
    technicalElement = models.ForeignKey("TechnicalElement", null=True, default=None, blank=True)
    sensor = models.ForeignKey("Sensor", null=True, default=None, blank=True)

    def __unicode__(self):
        return self.name
