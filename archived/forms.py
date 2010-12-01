#!/usr/bin/python
# -*- encoding: UTF-8 -*-

# -----------------------
# OpenEQ.org Project 2010
# Ron Elliott
# ron@openeq.org
# -----------------------

import web

regForm = web.form.Form(web.form.Textbox("email",
                                         description = "Email Address: "),
                        web.form.Password("password",
                                          description = "Password: "),
                        web.form.Password("passwordAgain",
                                          description = "Password Again: "),
                        web.form.Textbox("name",
                                         description = "Display name: "),
                        validators = [web.form.Validator("Passwords do not match!!", 
                                                         lambda i: i.password == i.passwordAgain)])

