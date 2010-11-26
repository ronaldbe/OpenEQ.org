#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

# -----------------------
# OpenEQ.org Project 2010
# Ron Elliott
# ron@openeq.org
# -----------------------

from xml.etree import ElementTree

import database

def _getDBObject(attribs = {}):
    type = attribs.pop("type")
    for dbObj in dir(database):
        if dbObj.lower().count("database") == 1:
            obj = getattr(database, dbObj)
            if hasattr(obj, "_type") and obj._type == type:
                return obj(**attribs)
    return None

def fillTestDataFromXML(xmlPath = ""):
    pass

def createFromXML(xmlPath = ""):
    rnode = ElementTree.parse(xmlPath).getroot()
    db = _getDBObject(rnode.attrib)
    for table in rnode.find("tables").findall("table"):
        tableName = table.attrib["name"]
        columns = {}
        for column in table.find("columns").findall("column"):
            columnName = column.attrib.pop("name")
            columns[columnName] = column.attrib
        db._createTable(tableName, columns)

if __name__ == "__main__":
    createFromXML("database.xml")

