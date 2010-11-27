#!/usr/bin/python
# -*- encoding: UTF-8 -*-

# -----------------------
# OpenEQ.org Project 2010
# Ron Elliott
# ron@openeq.org
# -----------------------

from sqlite3 import *
import web

from dbtypes import *

urls = (
    "/comment/(.*)", "comment",
    "/equation(.*)", "equation",
    "/user/(.*)", "user",
    "/(.*)", "index",
)

app = web.application(urls, globals())

def initDb(dbURI = "sqlite:///home/ron/Code/Python/openeq/openeq.sqlite"):
    sqlhub.processConnection = connectionForURI(dbURI)

class comment:
    def GET(self, id):
        comment = Comment.get(id)
        return comment

class equation:
    def GET(self, id):
        return "equation: %s" %id

class index: 
    def GET(self, id):
        initDb()
        renderer = web.template.render("templates/")
        return renderer.equationList("OpenEQ.org :: Home", Equation.select())

class user:
    def GET(self, id):
        return "user: %s" %id

#web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
if __name__ == "__main__":
    app.run()

