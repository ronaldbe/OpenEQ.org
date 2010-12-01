#!/usr/bin/python
# -*- encoding: UTF-8 -*-

# -----------------------
# OpenEQ.org Project 2010
# Ron Elliott
# ron@openeq.org
# -----------------------

import sqlobject

class User(sqlobject.SQLObject):
    canApprove   = sqlobject.BoolCol()
    canSubmit    = sqlobject.BoolCol()
    creationDate = sqlobject.DateTimeCol()
    email        = sqlobject.StringCol()
    enabled      = sqlobject.BoolCol()
    name         = sqlobject.StringCol()
    password     = sqlobject.StringCol()

