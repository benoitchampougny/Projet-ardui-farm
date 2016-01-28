from django.contrib import admin
from architect.models import Location, Network
# Register your models here.


admin.site.register(Location.Location)
admin.site.register(Location.TechnicalElement)
admin.site.register(Location.Measure)
admin.site.register(Network.Network)
admin.site.register(Network.ArduinoModel)
admin.site.register(Network.Arduino)
admin.site.register(Network.RaspberryModel)
admin.site.register(Network.Raspberry)
admin.site.register(Network.SensorModel)
admin.site.register(Network.Sensor)
admin.site.register(Network.Port)
admin.site.register(Network.I2cPort)
admin.site.register(Network.WifiPort)
admin.site.register(Network.Connection)
