import tornado.ioloop
import tornado.web

from remindr.handlers.main import (
    ItemHandler,
    MainHandler,
    UserHandler,
    UsersHandler,
)


UUID_REGEX = "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"


def make_app():
    return tornado.web.Application([
            (r"/", MainHandler),
            (r"/users/(%s)" % UUID_REGEX, UserHandler),
            (r"/users", UsersHandler),
            (r"/items", ItemHandler),
        ],
        autoreload=True,
        debug=True
    )

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()