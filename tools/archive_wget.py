#!/usr/bin/env python
import sys, os
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'
CMD_LINE='wget "http://%s" -rH -D%s --warc-file="%s" --warc-cdx --mirror -w 1 --random-wait -e robots=off -o %s.log --limit-rate=512k --cookies=on --keep-session-cookies --save-cookies=%s.cookie.txt --no-check-certificate -v --user-agent="%s"'


def run(domain):
	try:
		os.makedirs(domain)
	except OSError, e:
		print e
		pass
	os.chdir(domain)
#	url = 'http://www.%s' %(domain)
	os.system(CMD_LINE % (domain, domain, domain, domain, domain, USER_AGENT))
	os.chdir('..')
	
if __name__ == "__main__":
	run(sys.argv[1])