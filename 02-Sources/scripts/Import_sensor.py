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

datas= forDirectory("sensor")

for data in datas:
    if version(data, SensorModel, "model"):
            listInTupleExtract (data, SensorModel, Pin, PinFunction, "functions", "sensor", "model", "detailOfPin")
            listExtract (data, SensorModel, I2cAdress, "i2cAdress", "model", "adress I2c")
            listExtract (data, SensorModel, Measure, "measure", "model", "detailOfMeasure")
            sensorModelObj = SensorModel.objects.get(name=data["model"])
            elementObj = Element.objects.get(name=data["detailOfElement"])
            sensorModelObj.element = elementObj
            if data["detailOfBoolean"] != "":
                booleanObj = Boolean.objects.get(name=data["detailOfBoolean"])
                sensorModelObj.boolean = booleanObj
            sensorModelObj.save()

update(Update, "sensor")
