from twisted.web import server, resource
from twisted.internet import reactor, task, threads
from sys import argv

from Ping import Ping



class StatusResource(resource.Resource):
	isLeaf = True

	def render_GET(self, request):
		self.numberRequests += 1
		request.setHeader("context-type", "text/plain")
		return "X"


pinger = Ping()

def processPingResult(rc, host):
	print("%s - %d") % (host, rc)

def runEveryTenSeconds(host):
	d = threads.deferToThread(pinger.ping, host)
	d.addCallback(processPingResult, host)

loop = task.LoopingCall(runEveryTenSeconds, argv[1])
loopDeferred = loop.start(2.0)

reactor.listenTCP(8080, server.Site(StatusResource()))
reactor.run()
