# coding: utf-8

from handler.BaseHandlers import *

url = [
    (r'/', IndexHandler),
    (r'/webupdate', WebUpdate),
    (r'/console', Console),
    (r'/uphandler', UpHandler),
]