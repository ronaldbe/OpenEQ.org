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
    _classAttrs = { "_conn" : None,
                    "path"  : "./openeq.database", }
    _datatypeMap = { "boolean" : "BOOL",
                     "int"     : "INTEGER",
                     "varchar" : "VARCHAR", }
    _type = "sqlite3"


    def _buildCreateColumnSyntax(this, name = "", columns = {}):
        rval = "\"%s\" %s" %( name, this._datatypeMap[ columns["type"] ] )
        if columns.has_key("primary") and \
           columns["primary"].lower() == "true":
            rval += " PRIMARY KEY"
        if columns.has_key("auto-increment") and \
           columns["auto-increment"].lower() == "true":
            rval += " AUTOINCREMENT"
        if columns.has_key("null") and \
           columns["null"] == "false":
            rval += " NOT NULL"
        if columns.has_key("unique") and \
           columns["unique"].lower() == "true":
            rval += " UNIQUE"
        return rval

    def _createTable(this, name = "", columns = {}, dropFirst = True):
        if dropFirst:
            this._execute("DROP TABLE IF EXISTS \"%s\";\n" %name)
        cmd = "CREATE TABLE \"%s\" (" %name
        for column in columns.items():
            cmd += this._buildCreateColumnSyntax(column[0], column[1])
            cmd += ",\n"
        cmd += ");\n"
        print this._execute(cmd)

    def _connect(this):
        if this._conn != None:
            return
        this._conn = sqlite3.connect(this.path)

    def _disconnect(this):
        if this._conn == None:
            return
        this._conn.close()
        this._conn = None

    def _execute(this, cmd):
        results = None
        this._connect()
        try:
            results = this._conn.execute(cmd)
        except sqlite3.OperationalError as err:
            print "-" * 80
            print "ERROR: Execute command failed!!"
            print "%s" %cmd
            print "\n\n%s\n" %str(err)
            print "-" * 80
        this._disconnect()
        return results

    def get(this, indices = []):
        return []

    def put(this, values = []):
        return True

