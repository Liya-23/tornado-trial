import tornado.web 
import tornado.ioloop

class basicRequestHandler(tornado.web.Application):
    def get(self):
        self.write("the Fn Hero!!!")

class staticRequestHandler(tornado.web.Application):
    def get(self):
        self.render("index.html")
        
if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/", staticRequestHandler)  )
    ])
    
    app.listen(8881)
    print("im on port 8881")
    tornado.ioloop.IOLoop.current().start() 