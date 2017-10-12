# coding: utf-8

from handler.BaseHandlers import *

url = [
    (r'/', IndexHandler),
    (r'/console', Console),
    (r'/webuphandler', WebUpHandler),
    (r'/isexist', IsExist)
]