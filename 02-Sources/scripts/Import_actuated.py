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
  along with Arduifarm.  If not, see <http://www.gnu.org/licenses/>.
"""

from architect.models.Library import *
from scripts.Function import *



datas= forDirectory("actuator/actuated")

for data in datas:
    if version(data, ActuatedModel, "model"):
        actuatedObj = ActuatedModel.objects.get(name=data["model"])
        elementObj = Element.objects.get(name=data["detail influence element"])
        actuatedObj.brand = data["brand"]
        actuatedObj.element = elementObj
        flowActuator = data["flow actuator"]
        actuatedObj.save()
        for measure, direction in data["detail influence measure"].iteritems():
            measureObj = Measure.objects.get(name=measure)
            InfluenceMeasure.objects.create(actuated=actuatedObj, measure=measureObj, direction=direction)
        for measure, valueAndUnit in data["technicalCaracteristic"].iteritems():
            for value, unit in valueAndUnit.iteritems():
                measureObj = Measure.objects.get(name=measure)
                unitObj = Unit.objects.get(name=unit)
                technicalCaracteristicObj = TechnicalCaracteristic.objects.create(value=value, measure=measureObj, unit=unitObj, actuated=actuatedObj)

update(Update, "actuated")
