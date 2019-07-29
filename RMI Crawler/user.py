import Pyro4
import Pyro4.util
import sys
import time

from Frontier_Manager import Frontier_Manager
from pprint import pprint

sys.excepthook = Pyro4.util.excepthook


NUM_SERVERS = 2
crawler1 = Pyro4.Proxy("PYRONAME:server.crawler1")
crawler2 = Pyro4.Proxy("PYRONAME:server.crawler2")
crawler_list = [crawler1, crawler2]

global_seed_url = "http://www.vit.ac.in"

def pprint_data_to_file(data, fname):
	with open(fname, 'w') as out:
		pprint(data, stream=out)

def main():
	frm = Frontier_Manager(global_seed_url)
	
	currIndex = 0
	while currIndex < len(frm.frontier):
		for crawler in crawler_list:
			frm.crawl(currIndex, crawler)
			currIndex += 1
		# time.sleep(2)

	frm.crawl(0, crawler1)
	frm.print_details()

	pprint_data_to_file(frm.index_table, "pagetable.txt")
	pprint_data_to_file(frm.frontier, "frontier.txt")

if __name__ == "__main__":
	main()
