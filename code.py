#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

# -----------------------
# OpenEQ.org Project 2010
# Ron Elliott
# ron@openeq.org
# -----------------------

import web

from openeq.pages import *

urls = (
    "/user/login", "LoginUser",
)

app = web.application(urls, globals())
template = web.template.render("templates/")
#web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)

if __name__ == "__main__":
    app.run()

