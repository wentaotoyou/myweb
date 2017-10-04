# coding: utf-8

import tornado.web
import os
import ConfigParser


class MyConfigParser(ConfigParser.SafeConfigParser):
    def optionxform(self, optionstr):
        return optionstr

def parse_config():
    # config_file = os.path.join(__file__, './config)
    cp = MyConfigParser(allow_no_value=True)
    cp.read('conf/myweb.conf')
    protypes = {}
    protypes['soa'] = cp.options('soa')
    protypes['web'] = cp.options('web')
    return protypes

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        protypes = parse_config()
        self.render('index.html', protypes=protypes)


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
