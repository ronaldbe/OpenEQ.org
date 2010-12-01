#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

# -----------------------
# OpenEQ.org Project 2010
# Ron Elliott
# ron@openeq.org
# -----------------------

import sys; sys.path.append("~/Code/Python/openeq/")

from openeq.db import User

class LoginUser:
    def GET(self):
        return "Login"

