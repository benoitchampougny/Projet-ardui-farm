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

import json
import os

with open('../03-Library/update.json') as data_file:
    data=json.load(data_file)

orderingListImport = ["unit", "measure", "element", "I2cAdress", "boolean", "functionality", "groupFunction", "raspberry", "arduino", "sensor", "actuator", "shield", "actuated"]

version = data["version"]

updateFilter = Update.objects.filter(name="general update", version=version)

if not updateFilter:
    if data["total update"] == "False":
        totalUpdate = False
    if data["total update"] == "True":
        totalUpdate = True

    if  totalUpdate:
        for importName in orderingListImport:
            os.system("start /B python manage.py runscript Import_" + importName)
            updateFinish = False
            while not updateFinish:
                updateFinish = Update.objects.filter(name=importName, version=version)
    else:
        for importName in orderingListImport:
            for partialName in data["partial update"]:
                if importName == partialName:
                    orderingListImport.remove(importName)
                    os.system("start /B python manage.py runscript Import_" + importName )
                    updateFinish = False
                    while not updateFinish:
                        updateFinish = Update.objects.filter(name=importName, version=version)
        for importName in orderingListImport:
            update(Update, importName)

        update(Update, "general update")
