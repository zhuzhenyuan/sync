import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        num = self.get_argument('num')
        print(num)
        print(type(num))
        self.write({"text": "您猜了数字" + num})


def make_app():
    return tornado.web.Application([
        (r"/caishuzi", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
