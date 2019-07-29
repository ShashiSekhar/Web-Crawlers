import requests 
from bs4 import BeautifulSoup
try:
	# Python 3
	from urllib.parse import urlparse, urljoin
except ImportError:
	from urlparse import urljoin, urlparse

import Pyro4

@Pyro4.expose
class Crawler(object):
	def __init__(self):
		self.occupied_flag = False

	def is_occupied(self):
		return self.occupied_flag

	def seed_test(self, url):
		return True if self.hostname in url else False
		
	def get_all_urls(self, seed_url):
		self.occupied_flag = True
		self.seed_url = seed_url
		self.hostname = urlparse(seed_url).hostname

		try:
			page = requests.get(self.seed_url)
		except Exception as e:
			try:
				print("Failed to reached {}".format(url))
			except UnicodeEncodeError:
				print("Failed to reached and cant show the URL")
			return None

		if not (200 <= page.status_code <= 399):
			return None

		if 300 <= page.status_code <= 399:
			return None

		if "text/html" not in page.headers["content-type"]:
			return None

		soup = BeautifulSoup(page.text, 'html.parser')
		
		urls = []
		for link in soup.find_all('a', href=True):
			if link.get('href') in [None, "", "/"] or "#" in link.get('href'):
				continue
			# if self.seed_test(link.get('href')):
			urls.append(urljoin(self.hostname, link.get('href')))
		
		self.occupied_flag = False
		return [self.seed_url, list(set(urls))]

Pyro4.Daemon.serveSimple(
			{
				Crawler: "server.crawler2"
			},
			ns = True)

if __name__=="__main__":
	main()

