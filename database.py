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
    _type = "sqlite3"

    def _createTable(this, name, columns):
        print columns

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

