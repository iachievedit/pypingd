from twisted.web import server, resource
from twisted.internet import reactor

from Ping import Ping

class StatusResource(resource.Resource):
	isLeaf = True

	def render_GET(self, request):
		self.numberRequests += 1
		request.setHeader("context-type", "text/plain")
		return "X"


pinger = Ping()

reactor.callInThread(pinger.ping, "8.8.8.8")
reactor.listenTCP(8080, server.Site(StatusResource()))
reactor.run()
