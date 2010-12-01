#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

# -----------------------
# OpenEQ.org Project 2010
# Ron Elliott
# ron@openeq.org
# -----------------------

from comment import Comment
from equation import Equation
from user import User

def setupDb(dbURI = "sqlite:///home/ron/Code/Python/openeq/openeq.sqlite"):
    sqlhub.processConnection = connectionForURI(dbURI)

