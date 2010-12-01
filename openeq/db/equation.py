#!/usr/bin/python
# -*- encoding: UTF-8 -*-

# -----------------------
# OpenEQ.org Project 2010
# Ron Elliott
# ron@openeq.org
# -----------------------

import sqlobject

class Equation(sqlobject.SQLObject):
    approved         = sqlobject.BoolCol()
    approvedBy       = sqlobject.ForeignKey("User")
    createdBy        = sqlobject.ForeignKey("User")
    creationDate     = sqlobject.DateTimeCol()
    definition       = sqlobject.StringCol()
    description      = sqlobject.StringCol()
    enabled          = sqlobject.BoolCol()
    lastModifiedBy   = sqlobject.ForeignKey("User")
    lastModifiedDate = sqlobject.DateTimeCol()
    previousVersion  = sqlobject.ForeignKey("Equation")

