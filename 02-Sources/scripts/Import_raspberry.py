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

datas = forDirectory("raspberry")

for data in datas:
    if version(data, RaspberryModel, "model"):
        listInTupleExtract (data, RaspberryModel, Pin, PinFunction, "functions", "raspberry", "model", "detailOfPin")
        group(data, GroupFunctionModel, OptionalFunctionModel, RaspberryModel, PinFunction, Pin, PinGroup, "raspberry")



from architect.models.Library import *
from scripts.Function import *

datas = forDirectory("raspberry")

for data in datas:
    group(data, GroupFunctionModel, OptionalFunctionModel, RaspberryModel, PinFunction, Pin, PinGroup, "raspberry")
