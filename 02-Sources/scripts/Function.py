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
from datetime import datetime

def forDirectory (dir):
    directory = "../03-Library/" + dir +"/"
    files = os.listdir(directory)
    data = []
    for file in files:
        if file.endswith('.json'):
            with open(directory + file) as data_file:
                data.append(json.load(data_file))
    return data

def listInTupleExtract (data, Model, Pin, PinFunction, key, keyName, name, detailOfPin):
        modelObj = Model.objects.get(name=data[name])
        for pinNumber, functions in data[detailOfPin].iteritems():
            functionsObj = PinFunction.objects.filter(name__in=functions)
            pin = Pin.objects.create(number=pinNumber)
            exec("pin.%s=modelObj" % keyName)
            exec("pin.%s.add(*list(functionsObj))" % key)
            pin.save()

def listInTupleExtractShield (data, PinShield, ShieldModel, ArduinoModel, RaspberryModel, SensorModel, detailOfPin):
        shieldModelObj = ShieldModel.objects.get(name=data["model"])
        for sensor, pins in data[detailOfPin].iteritems():
            for pin in pins:
                controllerType = data["controller"]
                if controllerType == "arduino":
                    controllerModelOjb = ArduinoModel.objects.get(name=data["modelController"])
                if controllerType == "raspberry":
                    controllerModelOjb = RaspberryModel.objects.get(name=data["modelController"])
                sensorObj = SensorModel.objects.get(name=sensor)
                exec("PinShield.objects.create(number=pin, %s=controllerModelOjb, sensor=sensorObj, shield=shieldModelObj)" % controllerType)

def listExtract (data, Measure, Unit, key, nameobj, title):
        measureObj = Measure.objects.get(name=data[nameobj])
        for unit in data[title]:
                unitObj = Unit.objects.get(name=unit)
                exec("measureObj.%s.add(unitObj)" % key)

def tupleExtract (data, Model, name, title, titleTuple):
    modelobj = Model.objects.get(name=data[name])
    for a, b in data[titleTuple].iteritems():
        if a == title:
            exec("modelobj.%s=b" % title)
            modelobj.save()

def version(data, Model, name):
    modelobj = Model.objects.filter(name=data[name])
    number = 0
    dateNow = datetime.now()
    if modelobj:
        modelobj = Model.objects.get(name=data[name])
        if data['version'] > modelobj.version:
            versionType = "_old_version_"

        elif data['version'] < modelobj.version:
            versionType = "_deleted_version_"
        if data['version'] != modelobj.version:
            rename = data[name] + "_" + str(modelobj.version) + versionType + str(dateNow.year) + "-" + str(dateNow.month) + "-" + str(dateNow.day) + "(1)"
            modelFilter = Model.objects.filter(name=rename)
            while modelFilter:
                number = number + 1
                rename= data[name] + "_" + str(modelobj.version) + versionType + str(dateNow.year) + "-" + str(dateNow.month) + "-" + str(dateNow.day) + "(" + str(number) + ")"
                modelFilter = Model.objects.filter(name=rename)
            modelobj.name = rename
            modelobj.lastVersion = False
            modelobj.save()
            Model.objects.create(name=data[name], version=data['version'])
            return True

    elif not modelobj:
        Model.objects.create(name=data[name], version=data['version'])
        return True

    else:
        return False

def deleteOldVersion(Model, key, *args):
    modelOldVersion = Model.objects.filter(lastVersion=False)
    for oldVersion in modelOldVersion:
        relation = False
        modelObj = Model.objects.get(name=oldVersion)
        for modelRelation in args:
            modelRelationFilter = False
            exec("modelRelationFilter = modelRelation.objects.filter(%s=modelObj)" % key)
            if modelRelationFilter:
                relation = True
        if not relation:
            modelObj.delete()

def group(data, GroupFunctionModel, OptionalFunctionModel, ArduinoModel, PinFunction, Pin, PinGroup, controller):
    for groupfunction, pinfunction in data['detailOfGroup'].iteritems():
        number = 0
        for group in pinfunction:
            number = number+1
            for numberPin in group:
                groupFunctionModelObj = GroupFunctionModel.objects.get(name=groupfunction)
                controllerModelObj = ArduinoModel.objects.get(name=data['model'])
                exec("pinObj = Pin.objects.get(number=numberPin, %s=controllerModelObj)" % controller)
                exec("pinGroupObj, created = PinGroup.objects.get_or_create(number=number, groupFunctionModel=groupFunctionModelObj, %s=controllerModelObj)" % controller)
                pinGroupObj.pin.add(pinObj)
                pinGroupObj.save

def update(Update, importName):
    with open('../03-Library/update.json') as data_file:
        data=json.load(data_file)
    Update.objects.create(name=importName, version=data["version"])
