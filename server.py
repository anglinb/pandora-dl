#cherrypy server
import cherrypy

class HelloWorld(object):
	 @cherrypy.expose
	 def index(self):
		  return "Hello world!"

if __name__ == '__main__':
	cherrypy.server.socket_host: '0.0.0.0:8111'
	cherrypy.quickstart(HelloWorld())
