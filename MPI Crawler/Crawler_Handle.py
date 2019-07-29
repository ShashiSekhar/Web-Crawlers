import requests 
from bs4 import BeautifulSoup
try:
	# Python 3
	from urllib.parse import urlparse, urljoin
except ImportError:
	from urlparse import urljoin, urlparse
from pprint import pprint

from Crawler import Crawler
from mpi4py import MPI

comm = MPI.Comm.Get_parent()
size = comm.Get_size()
rank = comm.Get_rank()

url = comm.recv(source=0, tag=11)

clr = Crawler(url)
crawled_urls = clr.get_all_urls()

pprint(crawled_urls)
# comm.send(crawled_urls[0], dest=0, tag=12)

comm.Disconnect()