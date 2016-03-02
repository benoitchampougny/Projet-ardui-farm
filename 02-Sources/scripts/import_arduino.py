from architect.models.Library import *

import json
with open('../03-Library/arduino/uno.json') as data_file:
    data = json.load(data_file)


arduino, created = ArduinoModel.objects.get_or_create(name=data['model'])

if created:
    for pinNumber, functions in data['detail_of_pin_digital_IO'].iteritems():
        functionsObj = PinFunction.objects.filter(name__in=functions)
        pin = Pin.objects.create(number=pinNumber, arduino=arduino)
        pin.functions.add(*list(functionsObj))


print "done"
