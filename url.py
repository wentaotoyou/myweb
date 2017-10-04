# coding: utf-8

from handler.BaseHandlers import *

url = [
    (r'/', IndexHandler),
    (r'/test', Test),
    (r'/upweb.html', upweb),
    (r'/upproviders.html', upproviders),
    (r'/applist', AppList),
]