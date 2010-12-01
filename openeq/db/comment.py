#!/usr/bin/python
# -*- encoding: UTF-8 -*-

# -----------------------
# OpenEQ.org Project 2010
# Ron Elliott
# ron@openeq.org
# -----------------------

import sqlobject

class Comment(sqlobject.SQLObject):
    approved     = sqlobject.BoolCol()
    body         = sqlobject.StringCol()
    createdBy    = sqlobject.ForeignKey("User")
    creationDate = sqlobject.DateTimeCol()
    inReplyTo    = sqlobject.ForeignKey("Comment")

