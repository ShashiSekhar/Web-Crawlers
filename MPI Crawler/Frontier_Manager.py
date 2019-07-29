from pprint import pprint
from Crawler import Crawler

import requests 
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin


class Frontier_Manager():
	def __init__(self, seed_url):
		self.seed_url = seed_url
		self.hostname = urlparse(seed_url).hostname

		self.frontier = [seed_url]
		self.index_table = {}
		

	def write_to_frontier(self, seed_url, urls):
		# self.frontier_lock.acquire()
		oldfronlen = len(self.frontier)

		for url in urls:
			if url not in self.frontier:
				self.frontier.append(url)
		
		if len(self.frontier) - oldfronlen != 0:
			print("Added {} links to the frontier for {}".format(len(self.frontier)-oldfronlen, seed_url))
		# self.frontier_lock.release()

	def write_to_index_table(self, local_seed_url, urls):
		# self.index_lock.acquire()
		if local_seed_url not in self.index_table.keys():
			self.index_table[local_seed_url] = urls
		else:
			self.index_table[local_seed_url].extend(urls) 
		# self.index_lock.release()

	def make_writes(self, data):
		local_seed_url, urls = data[0], data[1]
		self.write_to_frontier(local_seed_url, urls)
		self.write_to_index_table(local_seed_url, urls)

	
	def crawl(self, local_seed_url):
		clr = Crawler(local_seed_url)
		return clr.get_all_urls(return_seed=True)
	

	def print_details(self):
		print("\nThe urls in the frontier are:")
		for url in self.frontier:
			print(url)

		print("\nThe index table generated is as follows:")
		for k in self.index_table.keys():
			print(k, ":")
			for url in self.index_table[k]:
				print('\t', url)
			