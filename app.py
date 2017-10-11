import os.path

# import tornado.httpserver
import tornado
# import tornado.options
import tornado.web

from url import url
import jenkins

from tornado.options import define, options

define("port", default=80, help='Run on the given port', type=int)

class Application(tornado.web.Application):
    def __init__(self):
        self.jenkins = jenkins.Jenkins

        handlers = url
        settings = {
            'template_path': os.path.join(os.path.dirname(__file__), "templates"),
            'static_path': os.path.join(os.path.dirname(__file__), "static")
        }

        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == '__main__':
    tornado.options.parse_command_line()

    # app = tornado.web.Application(
    #     # autoreload=True,
    #     handlers = url,
    #     template_path=os.path.join(os.path.dirname(__file__), "templates"),
    #     static_path=os.path.join(os.path.dirname(__file__), "static")
    # )
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    print 'Server started...'
