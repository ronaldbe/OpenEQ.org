#!/usr/bin/python
# -*- encoding: UTF-8 -*-

# -----------------------
# OpenEQ.org Project 2010
# Ron Elliott
# ron@openeq.org
# -----------------------

import web

urls = (
    "/comment/(.*)", "comment",
    "/equation(.*)", "equation",
    "/user/(.*)", "user",
    "/(.*)", "index",
)

app = web.application(urls, globals())

class comment:
    def GET(self, id):
        return "comment: %s" %id

class equation:
    def GET(self, id):
        return "equation: %s" %id

class index: 
    def GET(self, id):
        return 'index: %s' %id

class user:
    def GET(self, id):
        return "user: %s" %id

#web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
if __name__ == "__main__":
    app.run()

