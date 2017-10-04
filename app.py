import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=80, help='Run on the given port', type=int)

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

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers = [(r'/', IndexHandler),
                    (r'/test', Test),
                    (r'/upweb.html', upweb),
                    (r'/upproviders.html', upproviders),
                    ],
        template_path = os.path.join(os.path.dirname(__file__), "templates"),
        static_path = os.path.join(os.path.dirname(__file__), "static")
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    print 'Server started...'