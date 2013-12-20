#!/usr/bin/env python
import sys, os

CMD_LINE='wget -i %s -rH -D%s --warc-file="%s" --warc-cdx --mirror -w 1 --random-wait -e robots=off -o %s.log --limit-rate=512k --cookies=on --keep-session-cookies --save-cookies=%s.cookie.txt -v'


def run(domain, urllist):
	try:
		os.makedirs(domain)
	except OSError, e:
		print e
		pass
	os.chdir(domain)
#	url = 'http://www.%s' %(domain)
	os.system(CMD_LINE % (urllist,  domain, domain, domain, domain))
	os.chdir('..')
	
if __name__ == "__main__":
	run(sys.argv[1], sys.argv[2])