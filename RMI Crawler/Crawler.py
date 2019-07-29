import requests 
from bs4 import BeautifulSoup
try:
	# Python 3
	from urllib.parse import urlparse, urljoin
except ImportError:
	from urlparse import urljoin, urlparse


class Crawler(object):
	def __init__(self):
		pass

	def seed_test(self, url):
		return True if self.hostname in url else False
		
	def get_all_urls(self, seed_url, return_seed=False):
		
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

		soup = BeautifulSoup(page.text, 'html.parser')
		
		urls = []
		for link in soup.find_all('a', href=True):
			if link.get('href') in [None, "#", ""]:
				continue
			if self.seed_test(link.get('href')):
				# urls.append(urljoin(self.hostname, link.get('href')))
				urls.append(link.get('href'))
		
		if return_seed:
			return [self.seed_url, list(set(urls))]
		else:
			return urls

