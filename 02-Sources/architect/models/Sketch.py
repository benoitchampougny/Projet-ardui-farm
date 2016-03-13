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
    - the generation of arduino sketches,
"""
from django.db import models
from django.template import Template

class Sketch(models.Model):
    """
        Class that refere to an arduino model instance. Entry point to generates
        the sketch.
    """
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class SketchCode(models.Model):
    """
        Abstract class handle the rendering of sketch code.
        This object is includable from template thanks to the render methods.
    """
    sketch = models.OneToOneField(Sketch)
    code = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return str(self.sketch) + " " + self.__class__.__name__.lower()

    def render(self, context):
        return Template(self.code).render(context)


class Header(SketchCode):
    """
        Class the generate the sketch header:
            - #include(s)
            - #define(s)
            - init vars
    """
    pass


class Setup(SketchCode):
    """
        Class the generate the parts of the sketch setup function
    """
    pass


class Loop(SketchCode):
    """
        Class the generate the parts of the sketch loop function
    """
    pass
