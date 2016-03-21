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
    Define the dataframe for message exchange between components.
"""
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Message(models.Model):
    name = models.CharField(max_length=100)
    label = models.IntegerField(validators=[MaxValueValidator(255)])
    sdi = models.IntegerField(validators=[MaxValueValidator(3)])
    ssm = models.IntegerField(validators=[MaxValueValidator(3)])

    def __unicode__(self):
        return "%s [%s]" % (self.name, str(self.label))

class Data(models.Model):
    message = models.ForeignKey('Message')
    name = models.CharField(max_length=100)
    lsb = models.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(29)])
    msb = models.IntegerField(validators=[MinValueValidator(10), MaxValueValidator(29)])
    units = models.ForeignKey('Units', null=True, default=None, blank=True)
    scale = models.DecimalField(default=1, max_digits=7, decimal_places=2)

    class Meta:
        ordering = ['lsb']
        abstract = True

    def __unicode__(self):
        return "%s: %s" % (self.message, self.name)

class Units(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class BCDData(Data):
    decimalPlaces = models.IntegerField(default=0)
