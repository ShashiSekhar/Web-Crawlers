from mpi4py import MPI
from mpi4py.futures import MPIPoolExecutor
import sys 

from Frontier_Manager import Frontier_Manager
from pprint import pprint


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

num_procs = 5
global_seed_url = "http://www.vit.ac.in"
frm = Frontier_Manager(global_seed_url)

def crawler_handler(seed_url):
	comm.send()



# def crawl(seed_url):
# 	clr = Crawler(seed_url)
# 	return clr.get_all_urls(return_seed=True)

if __name__ == "__main__":
	oldFron = None
	with MPIPoolExecutor(num_procs) as executor:
		while oldFron != frm.frontier:
			oldFron = frm.frontier
			mapper = executor.map(frm.crawl, frm.frontier)
			for data in mapper:
				# print(data)
				frm.make_writes(data)


	frm.print_details()