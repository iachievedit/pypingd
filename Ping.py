# https://stackoverflow.com/questions/2953462/pinging-servers-in-python/32684938#32684938

import subprocess
from sys import argv

class Ping:
	def __init__(self):
		pass

	def ping(self, host):
	    """
	    Returns 0 if host (str) responds to a ping request, non-zero integer otherwise
	    """

	    # Pinging
	    proc = subprocess.Popen(["ping", "-t1", "-c1", "-o", host], stdout=subprocess.PIPE)
	    output = proc.communicate()[0] # Debugging only when we want to 
	    print output
	    return proc.returncode

if __name__ == "__main__":
	host = argv[1]

	pinger = Ping()
	rc = pinger.ping(host)
	print rc

	if rc == 0:
		print "Response"
	else:
		print "Error"