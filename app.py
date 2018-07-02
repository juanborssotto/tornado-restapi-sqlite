from tornado.ioloop import IOLoop
import tornado.web
from repository import repo
from domain import service


import sqlite3 as sqlite


class DishHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self, restaurant, id):
        if id is None:
            #Raise exception
            self.write('id is missing')
            self.finish()
        repository = repo.Repo()
        svc = service.Service(repository)
        dish = svc.getDish(restaurant, id)
        self.write({'dish': dish})
        self.finish()

    @tornado.web.asynchronous
    def post(self, restaurant, id):
        if id is not None:
            #Raise exception
            self.write('ID should not be in the URL')
            self.finish()
        repository = repo.Repo()
        svc = service.Service(repository)
        bodyData = tornado.escape.json_decode(self.request.body)
        try:
            dish = svc.insertDish(restaurant, bodyData['name'], bodyData['description'], bodyData['price'])
            self.write({'dish': dish})
        except:
            self.write('Incorrect post parameters')
        finally:
            self.finish()


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/([a-z]+)/dish/([0-9]+)?", DishHandler)
        ]
        tornado.web.Application.__init__(self, handlers)


def main():
    app = Application()
    app.listen(8888)
    IOLoop.instance().start()


if __name__ == '__main__':
    main()
