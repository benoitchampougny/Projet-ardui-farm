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
      along with Arduifarm.  If not, see <http://www.gnu.org/licenses/>. 2
"""
"""
    This file will contain models that are related to
    - space, area, room, etc
        To define where network element is located
    - The sementic name of a measure or of an element for example Temperature, Engine, etc
"""
from django.db import models
from architect.models.Network import Sensor
from architect.models.Network import Actuator
from django.utils.deconstruct import deconstructible

class Location(models.Model):
    name = models.CharField("Location Name", max_length=200)
    master = models.ForeignKey('Environment', null=True, default=None, blank=True)

    def __unicode__(self):
        return self.name

@deconstructible
class LocationComponent(object):
    """ Class to define common methods between components  """
    def __unicode__(self):
        return self.name

    def _get_component_name(self):
        return self.__class__.__name__

    def tree_element_template(self):
        component = self._get_component_name()
        return "location/%s/tree_element.html" % component

    def detail_element_template(self):
        component = self._get_component_name()
        return "location/%s/element_details.html" % component

    def component_type(self):
        return self._get_component_name()

class Zone(models.Model, LocationComponent):
    name = models.CharField("Location Name", max_length=200)
    locationPorts = models.ManyToManyField("LocationPort", blank=True)

    def downLocation(self):
        return self.locationPorts.filter(direction="DW")

class Environment(models.Model, LocationComponent):
    name = models.CharField("Location Name", max_length=200)
    locationPorts = models.ManyToManyField("LocationPort", blank=True)

    def downLocation(self):
        return self.locationPorts.filter(direction="DW")

class Scenario(models.Model, LocationComponent):
    name = models.CharField("Scenario Name", max_length=200)
    locationPorts = models.ManyToManyField("LocationPort", blank=True)

    def downLocation(self):
        return self.locationPorts.filter(direction="DW")

class GenericPort(models.Model):
    DIRECTIONS = (
        ("UP", "Upward"),
        ("DW", "Downward"),
    )
    direction = models.CharField(max_length=2, choices=DIRECTIONS, default="DW")
    address = models.CharField("Address", max_length=200, default=None, blank=True, null=True)
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


class LocationPort(GenericPort):
    @property
    def parent(self):
        return self._get_parent(['zone', 'environment', 'sensor', 'actuator', 'scenario'])
