#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

# -----------------------
# OpenEQ.org Project 2010
# Ron Elliott
# ron@openeq.org
# -----------------------

import sqlite3

import baseobject

class MySQLDatabase(baseobject.BaseObject):
    _classAttrs = { "address" : "",
                    "password" : "",
                    "path" : "",
                    "username" : "", }
    _type = "mysql"

    def get(this, indices = []):
        return []

    def put(this, values = []):
        return True

class SQLiteDatabase(baseobject.BaseObject):
    _classAttrs = { "_conn"        : None,
                    "path" : "./database.db", }
    _datatypeMap = { "boolean" : "BOOL",
                     "int"     : "INTEGER",
                     "varchar" : "TEXT", }
    _type = "sqlite3"


    def _buildCreateColumnSyntax(this, name = "", columns = {}):
        rval = "%s %s" %( name, this._datatypeMap[ columns["type"] ] )
        if columns["primary"].lower() == "true":
            rval += " PRIMARY KEY"
        return rval

    def _createTable(this, name = "", columns = {}):
        cmd = "CREATE TABLE %s (" %name
        for column in columns.items():
            cmd += this._buildCreateColumnSyntax(column[0], column[1])
            cmd += ",\n"
        cmd += ")"
        print cmd

    def _connect(this):
        if this != None:
            return
        this._conn = sqlite3.connect(this.databasePath)

    def _disconnect(this):
        this._conn.close()
        this._conn = None

    def get(this, indices = []):
        return []

    def put(this, values = []):
        return True

