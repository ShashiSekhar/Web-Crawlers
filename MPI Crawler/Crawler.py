import requests 
from bs4 import BeautifulSoup
try:
	# Python 3
	from urllib.parse import urlparse, urljoin
except ImportError:
	from urlparse import urljoin, urlparse


class Crawler(object):
	def __init__(self, seed_url, hostname=None):
		self.seed_url = seed_url
		if hostname == None:
			self.hostname = urlparse(seed_url).hostname
		else:
			self.hostname = hostname

	def seed_test(self, url):
		return True if self.hostname in url else False
		
	def get_all_urls(self, return_seed=False):
		try:
			page = requests.get(self.seed_url)
		except Exception as e:
			try:
				print("Failed to reached {}".format(url))
			except UnicodeEncodeError:
				print("Failed to reached and cant show the URL")
			return None

		soup = BeautifulSoup(page.text, 'html.parser')
		
		urls = []
		for link in soup.find_all('a', href=True):
			if link.get('href') in [None, "#", ""]:
				continue
			if self.seed_test(link.get('href')):
				urls.append(urljoin(self.seed_url, link.get('href')))
		
		if return_seed:
			return [self.seed_url, list(set(urls))]
		else:
			return urls

