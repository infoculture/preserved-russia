#!/usr/bin/env python
import sys, os

CMD_LINE="httrack --connection-per-second=50 --sockets=15 --keep-alive --display --verbose --advanced-progressinfo --disable-security-limits -n -i -s0 -m -F 'Mozilla/5.0 (X11;U; Linux i686; en-GB; rv:1.9.1) Gecko/20090624 Ubuntu/9.04 (jaunty) Firefox/3.5' --max-rate=1000000 %s"


def run(domain):
	try:
		os.makedirs(domain)
	except OSError:
		pass
	os.chdir(domain)
	url = 'http://www.%s' %(domain)
	os.system(CMD_LINE % url)
	os.chdir('..')
	
if __name__ == "__main__":
	run(sys.argv[1])