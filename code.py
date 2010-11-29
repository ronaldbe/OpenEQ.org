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
    "/comment/view/(.*)", "ViewComment",
    "/equation/add", "AddEquation",
    "/equation/edit/(.*)/", "EditEquation",
    "/equation/view/(.*)", "ViewEquation",
    "/user/login", "LoginUser",
    "/user/register", "RegisterUser",
    "/user/view/(.*)", "ViewUser",
    "/(.*)", "index",
)

app = web.application(urls, globals())
template = web.template.render("templates/")

def initDb(dbURI = "sqlite:///home/ron/Code/Python/openeq/openeq.sqlite"):
    sqlhub.processConnection = connectionForURI(dbURI)

class AddEquation:
    def GET(self):
        return "HELLO!!"

    def POST(self):
        pass

class EditEquation:
    def GET(self):
        return "HELLO!!"

    def POST(self):
        pass

class Index:
    def GET(self, id):
        initDb()
        return template.equationList("Home", Equation.select())

class LoginUser:
    def GET(self):
        pass

class RegisterUser:
    def GET(self):
        return template.register("New User Registration")

    def POST(self):
        pass

class ViewComment:
    def GET(self, id):
        comment = Comment.get(id)
        return comment

class ViewEquation:
    def GET(self, id):
        initDb()
        return template.equation( "OpenEQ.org :: ", Equation.get( int(id) ) )

class ViewUser:
    def GET(self, id):
        return "user: %s" %id

#web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
if __name__ == "__main__":
    app.run()

