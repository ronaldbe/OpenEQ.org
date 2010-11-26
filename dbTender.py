#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

# -----------------------
# OpenEQ.org Project 2010
# Ron Elliott
# ron@openeq.org
# -----------------------

import optparse
from sqlobject import *
from xml.etree import ElementTree

import dbtypes

def connect(xmlPath = ""):
    dbNode = ElementTree.parse(xmlPath).getroot().find("database")
    params = { 
        "database" : "",
        "host" : "",
        "password" : "",
        "port" : "",
        "scheme" : "",
        "username" : "", }
    params.update(dbNode.attrib)
    username = params["username"]
    password = ""
    if params["password"] != "":
        password = ":%s@" %params["password"]
    else:
        if username != "":
            password = "@"
    port = ""
    if params["port"] != "":
        port = ":%s" %params["port"]
    uri = "%s://%s%s%s%s/%s" %(params["scheme"],
                                  username,
                                  password,
                                  params["host"],
                                  port,
                                  params["database"])
    print "Connecting to '%s'..." %uri
    sqlhub.processConnection = connectionForURI(uri)

def createTables(xmlPath = ""):
    print "Creating table for 'Comment'...",
    print dbtypes.Comment.createTable()
    print "Creating table for 'Equation'...",
    print dbtypes.Equation.createTable()
    print "Creating table for 'User'...",
    print dbtypes.User.createTable()

def dropTables(xmlPath = ""):
    print "Dropping table for 'Comment'...",
    print dbtypes.Comment.dropTable(ifExists = True)
    print "Dropping table for 'Equation'...",
    print dbtypes.Equation.dropTable(ifExists = True)
    print "Dropping table for 'User'...",
    print dbtypes.User.dropTable(ifExists = True)

def loadTestData(xmlPath = ""):
    rnode = ElementTree.parse(xmlPath).getroot()
    for child in rnode:
        if child.tag == "database":
            continue
        if not hasattr(dbtypes, child.tag.capitalize()):
            continue
        type = getattr(dbtypes, child.tag.capitalize())
        type(**child.attrib)
        print "Created type '%s'" %type

if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option("-c", "--create", action = "store_true", default = False, dest = "create", help = "Create the tables.")
    parser.add_option("-d", "--drop", action = "store_true", default = False, dest = "drop", help = "Drop the tables.")
    parser.add_option("-l", "--load", action = "store_true", default = False, dest = "load", help = "Load the test data.")
    parser.add_option("-r", "--refresh", action = "store_true", default = False, dest = "refresh", help = "Refresh the database. Same as --drop --create and --load")
    parser.add_option("-x", "--xml", dest = "xmlPath", help = "The XML file to use as input.")
    (options, args) = parser.parse_args()
    connect(options.xmlPath)
    if options.refresh:
        options.create = True
        options.drop = True
        options.load = True
    if options.drop:
        dropTables(options.xmlPath)
    if options.create:
        createTables(options.xmlPath)
    if options.load:
        loadTestData(options.xmlPath)

