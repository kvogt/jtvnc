import cherrypy
import gui

cherrypy.config.update({
    'server.socket_host': '0.0.0.0',
    'server.socket_port': 8000,
    'server.thread_pool': 10,
})

class Server:

    @cherrypy.expose
    def index(self):
        return "JTVNC v0.1"

    @cherrypy.expose
    def move(self, x=None, y=None):
        gui.move(x, y)
        return "Moved mouse to %s, %s." % (x, y)

    @cherrypy.expose
    def down(self, x=None, y=None):
        gui._down(x, y)
        return "Mouse down at %s, %s." % (x, y)

    @cherrypy.expose
    def up(self, x=None, y=None):
        gui._up(x, y)
        return "Mouse up at %s, %s." % (x, y)

    @cherrypy.expose
    def keydown(self, id=None):
        gui._keydown(id)
        return "Key id %s pressed." % id

    @cherrypy.expose
    def keyup(self, id=None):
        gui._keyup(id)
        return "Key id %s depressed." % id

    @cherrypy.expose
    def click(self, x=None, y=None, delay=0.1):
        gui.click(x, y, delay)
        return "Clicked at %s, %s." % (x, y)

cherrypy.quickstart(Server())