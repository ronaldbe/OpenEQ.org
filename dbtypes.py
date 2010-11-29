#!/usr/bin/python
# -*- encoding: UTF-8 -*-

# -----------------------
# OpenEQ.org Project 2010
# Ron Elliott
# ron@openeq.org
# -----------------------

from sqlobject import *

class Comment(SQLObject):
    approved     = BoolCol()
    body         = StringCol()
    createdBy    = ForeignKey("User")
    creationDate = DateTimeCol()
    inReplyTo    = ForeignKey("Comment")

class Equation(SQLObject):
    approved         = BoolCol()
    body             = StringCol()
    createdBy        = ForeignKey("User")
    creationDate     = DateTimeCol()
    description      = StringCol()
    lastModifiedBy   = ForeignKey("User")
    lastModifiedDate = DateTimeCol()

class User(SQLObject):
    canApprove = BoolCol()
    canSubmit  = BoolCol()
    email      = StringCol()
    enabled    = BoolCol()
    name       = StringCol()
    password   = StringCol()
    username   = StringCol()

