import tornado.web
import tornado.ioloop


class BasicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World!")


class StaticRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class QueryStringRequestHandler(tornado.web.RequestHandler):
    def get(self):
        num = int(self.get_argument("num"))
        res = "even" if num % 2 == 0 else "odd"
        self.write(f"The number {num} is {res}")


class ResourceRequestHandler(tornado.web.RequestHandler):
    def get(self, id_):
        self.write(f"Querying tweet with id {id_}")


if __name__ == '__main__':
    app = tornado.web.Application([
        (r"/", BasicRequestHandler),
        (r"/blog", StaticRequestHandler),
        (r"/is-even", QueryStringRequestHandler),
        (r"/tweet/([0-9]+)", ResourceRequestHandler)
    ])

    PORT = 8888

    app.listen(PORT)
    print(f"[LISTENING] Listening on port {PORT}")
    tornado.ioloop.IOLoop.current().start()
