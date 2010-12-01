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
from forms import *

urls = (
    "/comment/view/(.*)", "ViewComment",
    "/equation/add", "AddEquation",
    "/equation/edit/(.*)/", "EditEquation",
    "/equation/view/(.*)", "ViewEquation",
    "/user/edit/(.*)", "EditUser",
    "/user/login", "LoginUser",
    "/user/register", "RegisterUser",
    "/user/view/(.*)", "ViewUser",
    "/(.*)", "index",
)

app = web.application(urls, globals())
template = web.template.render("templates/")

dbURI = "sqlite:///home/ron/Code/Python/openeq/openeq.sqlite"
sqlhub.processConnection = connectionForURI(dbURI)

class ViewComment:
    def GET(self, id):
        comment = Comment.get(id)
        return comment

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

class ViewEquation:
    def GET(self, id):
        return template.ViewEquation( "OpenEQ.org :: ", Equation.get( int(id) ) )

class Index:
    def GET(self, id):
        return template.Index("Home", Equation.select())

class EditUser:
    def GET(self, email):
        return template.EditUser("Edit User")

class LoginUser:
    def GET(self):
        pass

class RegisterUser:
    def GET(self):
        return template.RegisterUser("New User Registration", regForm)

    def POST(self):
        newUserInfo = regForm()
        if not newUserInfo.validates():
            return template.RegisterUser("New User Registration", newUserInfo)
        newUser = User(**newUserInfo.d)
        if newUser != None:
            return template.blank("Registration successfull!! Please <a href=\"/user/login\">login</a>.")
        return template.RegisterUser("New User Registration", newUserInfo)

class ViewUser:
    def GET(self, id):
        return "user: %s" %id

#web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
if __name__ == "__main__":
    app.run()

