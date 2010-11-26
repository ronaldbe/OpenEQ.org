#!/usr/bin/python
# -*- encoding: UTF-8 -*-

# -----------------------
# OpenEQ.org Project 2010
# Ron Elliott
# ron@openeq.org
# -----------------------

import web

urls = (
    "/.*", "hello"
    )
app = web.application(urls, globals())

class hello: 
    def GET(self):
        return 'Hello, world!'

#web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
if __name__ == "__main__":
    app.run()

