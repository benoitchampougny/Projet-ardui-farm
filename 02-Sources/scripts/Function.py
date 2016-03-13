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

import json
import os

def forDirectory (dir):
    directory = "../03-Library/" + dir +"/"
    files = os.listdir(directory)
    data = []
    for file in files:
        if file.endswith('.json'):
            with open(directory + file) as data_file:
                data.append(json.load(data_file))
    return data

def digitalControlerPinArduino (datas, model, PinFunction, Pin, detailOfPin):
    for data in datas:
        arduino = model.objects.create(name=data['model'])
        for pinNumber, functions in data[detailOfPin].iteritems():
            functionsObj = PinFunction.objects.filter(name__in=functions)
            pin = Pin.objects.create(number=pinNumber, arduino=arduino)
            pin.functions.add(*list(functionsObj))

def digitalControlerPinRaspberry (datas, model, PinFunction, Pin, detailOfPin):
    for data in datas:
        raspberry = model.objects.create(name=data['model'])
        for pinNumber, functions in data[detailOfPin].iteritems():
            functionsObj = PinFunction.objects.filter(name__in=functions)
            pin = Pin.objects.create(number=pinNumber, raspberry=raspberry)
            pin.functions.add(*list(functionsObj))

def digitalControlerPinSensor (datas, model, PinFunction, Pin, detailOfPin):
    for data in datas:
        sensor = model.objects.create(name=data['model'])
        for pinNumber, functions in data[detailOfPin].iteritems():
            functionsObj = PinFunction.objects.filter(name__in=functions)
            pin = Pin.objects.create(number=pinNumber, sensor=sensor)
            pin.functions.add(*list(functionsObj))

def listExtract (datas, Measure, Unit, key, nameobj, title):
    for data in datas:
        measure = Measure.objects.get(name=data[nameobj])
        for unit in data[title]:
                unitobj = Unit.objects.get(name=unit)
                exec("measure.%s.add(unitobj)" % key)

def groupFunctionality (datas,GroupFunctionModel, PinFunction, title):
    for data in datas:
        if data[title]:
            optionalfunctionmodel = GroupFunctionModel.objects.create(name=data['name'], version=data['version'])
            for pinfunction in data[title]:
                    pinfunctionobj =PinFunction.objects.get(name=pinfunction)
                    optionalfunctionmodel.pinfunction.add(pinfunctionobj)

def grpOptFunctionality(datas, GroupFunctionModel, OptionalFunctionModel):
    for data in datas:
        if data['optionalFunctionality']:
                groupfunctionmodelobj = GroupFunctionModel.objects.get(name=data['name'])
                optionalfunctionmodelobj = OptionalFunctionModel.objects.get(name=data['name'])
                groupfunctionmodelobj.optionalFunctionModel=optionalfunctionmodelobj
                groupfunctionmodelobj.save()

def tupleExtract (datas, Model, name, title, titleTuple):
    for data in datas:
        modelobj = Model.objects.get(name=data[name])
        for a, b in data[titleTuple].iteritems():
            if a == title:
                exec("modelobj.%s=b" % title)
                modelobj.save()

def version(datas, Model):
    for data in datas:
        modelobj = Model.objects.get(name=data['name'])
        if data['version'] > modelobj.version:
                groupfunctionmodelobj = GroupFunctionModel.objects.get(name=data['name'])
                optionalfunctionmodelobj = OptionalFunctionModel.objects.get(name=data['name'])
                groupfunctionmodelobj.optionalFunctionModel=optionalfunctionmodelobj
                groupfunctionmodelobj.save()


def createName (datas, Model, name):
    for data in datas:
        modelobj = Model.objects.create(name=data[name])
