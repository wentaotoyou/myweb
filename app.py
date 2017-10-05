import os.path

# import tornado.httpserver
import tornado
# import tornado.options
import tornado.web

from url import url

from tornado.options import define, options

define("port", default=80, help='Run on the given port', type=int)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        # autoreload=True,
        handlers=url,
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static")
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    print 'Server started...'
