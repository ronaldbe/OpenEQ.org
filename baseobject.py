#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

# -----------------------
# OpenEQ.org Project 2010
# Ron Elliott
# ron@openeq.org
# -----------------------

class BaseObject(object):
    _classAttrs = {}

    def __init__(this, **kwds):
        super(BaseObject, this).__init__()
        if hasattr(this, "_classAttrs"):
            for attrSet in this._classAttrs.items():
                setattr(this, attrSet[0], attrSet[1])
        if hasattr(this, "_preInit"):
            this.preInit()
        for kwdSet in kwds.items():
            if hasattr(this, kwdSet[0]):
                setattr(this, kwdSet[0], kwdSet[1])
        if hasattr(this, "_postInit"):
            this._postInit()

