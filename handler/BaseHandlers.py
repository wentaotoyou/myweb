# coding: utf-8

import tornado
import tornado.web
import tornado.websocket
import os
import ConfigParser


# from functions import compile

class MyConfigParser(ConfigParser.SafeConfigParser):
    def optionxform(self, optionstr):
        return optionstr


# read the config file
def parse_config():
    cp = MyConfigParser(allow_no_value=True)
    cp.read('conf/myweb.conf')
    protypes = {}
    protypes['soa'] = cp.options('soa')
    protypes['web'] = cp.options('web')
    return protypes


class Console(tornado.web.RequestHandler):
    def get(self):
        self.render('console.html')


class UpHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        # self.write_message('open')
        pass

    def on_message(self, message):
        self.write_message('copy that %s' % message)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        protypes = parse_config()
        self.render('index.html', protypes=protypes)


class WebUpdate(tornado.web.RequestHandler):
    def post(self):
        isupdate = self.get_argument('web_input_isupdate')
        app = self.get_argument('web_input_app')
        filelist = self.get_argument('web_txtarea_after')
        filelist = filelist.split('\n')

        notexist = []
        for file in filelist:
            file_path = os.path.join('e:\\', app, file)
            if not os.path.isfile(file_path):
                notexist.append(file_path)

        if notexist and isupdate == '0':
            cb = {"status_code": 405, "filelist": notexist}
        else:
            cb = {"status_code": 200}

        print cb
        self.write(cb)
