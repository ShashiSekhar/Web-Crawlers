
from pprint import pprint
import time

import requests 
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def pprint_data_to_file(data, fname):
	with open(fname, 'w') as out:
		pprint(data, stream=out)

class Frontier_Manager():
	def __init__(self, seed_url):
		self.seed_url = seed_url
		self.hostname = urlparse(seed_url).hostname

		self.frontier = [seed_url]
		self.index_table = dict()
		

	def seed_test(self, url):
		return True if self.hostname in url else False

	def write_to_frontier(self, seed_url, urls):
		oldFronLen = len(self.frontier)

		for url in urls:
			if url not in self.frontier and self.seed_test(url):
				self.frontier.append(url.strip())
		
		if len(self.frontier) > oldFronLen: 
			try:
				print("Added {} links in the frontier for the link: {}".format(len(self.frontier)-oldFronLen, seed_url))
			except UnicodeEncodeError:
				print("Added {} links in the frontier for the link: NOT ABLE TO PRINT".format(len(self.frontier)-oldFronLen))

		self.frontier = list(set(self.frontier))


	def write_to_index_table(self, local_seed_url, urls):
		if local_seed_url not in self.index_table.keys():
			self.index_table[local_seed_url] = urls
		else:
			self.index_table[local_seed_url].extend(urls) 

	def make_writes(self, data):
		local_seed_url, urls = data[0], data[1]
		self.write_to_frontier(local_seed_url, urls)
		self.write_to_index_table(local_seed_url, urls)


	def crawl(self, index, crawler):
		try:
			url = self.frontier[index]
			# print("Going to crawl: ", url)
			pprint_data_to_file("Going to crawl: {}".format(url), "vit.log")
		except IndexError:
			print("Index Error Occured. Moving on.")
			return;

		try:
			data = crawler.get_all_urls(url)
			if data:
				self.make_writes(data)			
		except Exception as e:
			print("Exception {} has occured for the url [{}], moving on.".format(e, url))

	def print_details(self):
		print("\nThe urls in the frontier are:")
		for url in self.frontier:
			print(url)

		print("\nThe index table generated is as follows:")
		for k in self.index_table.keys():
			print(k, ":")
			for url in self.index_table[k]:
				print('\t', url)

