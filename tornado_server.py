import os
import tornado.httpserver
import tornado.httpclient
import tornado.ioloop
import tornado.options
import tornado.web

import logging

# settings is required/used to set our environment
import settings 

import controllers.basic
import controllers.general

class Application(tornado.web.Application):
  def __init__(self):

    debug = (tornado.options.options.environment == "dev")

    app_settings = {
      "cookie_secret" : os.environ['COOKIE_SECRET'].strip(),
      "login_url": "/",
      "debug": debug,
      "static_path" : os.path.join(os.path.dirname(__file__), "static"),
      "template_path" : os.path.join(os.path.dirname(__file__), "views"),
    }

    """
    the endpoints this torando instance provides
      1. this is a drop through list (first thing it matches is the path it will take)
      2. supports regular expressions (so the last line essentially catches any/all requests to this application and rountes the user to the not found controller)
    """
    handlers = [
      (r"/test/mongo", controllers.general.TestMongo),
      (r".+", controllers.general.NotFound),
    ]

    tornado.web.Application.__init__(self, handlers, **app_settings)

def main():
  tornado.options.define("port", default=8001, help="Listen on port", type=int)
  tornado.options.parse_command_line()
  logging.info("starting tornado_server on 0.0.0.0:%d" % tornado.options.options.port)
  http_server = tornado.httpserver.HTTPServer(request_callback=Application(), xheaders=True)
  http_server.listen(tornado.options.options.port)
  tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
  main()
