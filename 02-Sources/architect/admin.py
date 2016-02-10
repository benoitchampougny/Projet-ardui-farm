from django.contrib import admin
from architect.models import Location, Network, Library
# Register your models here.


# Location package
admin.site.register(Location.Location)
admin.site.register(Location.TechnicalElement)
admin.site.register(Location.Measure)

# Network package
admin.site.register(Network.Network)
admin.site.register(Network.Arduino)
admin.site.register(Network.Raspberry)
admin.site.register(Network.Sensor)
admin.site.register(Network.I2cPort)
admin.site.register(Network.WifiPort)

# Library package
admin.site.register(Library.RaspberryModel)
admin.site.register(Library.ArduinoModel)
admin.site.register(Library.SensorModel)
admin.site.register(Library.Pin)
admin.site.register(Library.PinFunction)
