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
