from django.contrib import admin
from architect.models import Location, Network, Library, Message
# Register your models here.


# Location package
admin.site.register(Location.Location)
admin.site.register(Location.Environment)
admin.site.register(Location.Zone)
admin.site.register(Location.LocationPort)
admin.site.register(Location.Scenario)


# Network package
admin.site.register(Network.Network)
admin.site.register(Network.Arduino)
admin.site.register(Network.Raspberry)
admin.site.register(Network.Sensor)
admin.site.register(Network.I2cPort)
admin.site.register(Network.DigitalPort)
admin.site.register(Network.WifiPort)
admin.site.register(Network.Actuator)

# Library package
admin.site.register(Library.RaspberryModel)
admin.site.register(Library.ArduinoModel)
admin.site.register(Library.SensorModel)
admin.site.register(Library.ActuatorModel)
admin.site.register(Library.Pin)
admin.site.register(Library.PinFunction)

# Message
admin.site.register(Message.Message)
admin.site.register(Message.BCDData)
admin.site.register(Message.Units)
