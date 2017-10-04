# coding: utf-8

import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


class Test(tornado.web.RequestHandler):
    def post(self):
        filelist = self.get_argument('filelist')
        print type(filelist)


class upweb(tornado.web.RequestHandler):
    def get(self):
        self.render('upweb.html')


class upproviders(tornado.web.RequestHandler):
    def get(self):
        self.render('upproviders.html')


class AppList(tornado.web.RequestHandler):
    def get(self):
        protype = self.get_argument('protype')
        if protype == "web":
            self.write('web')
        else:
            self.write('soa')
