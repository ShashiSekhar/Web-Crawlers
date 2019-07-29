from mpi4py import MPI
import numpy as np

# comm = MPI.COMM_WORLD
# rank = comm.Get_rank()
# size = comm.Get_size()


# if rank == 0:
#     data = {'a': 7, 'b': "BLABLA"}
#     comm.send(data, dest=1, tag=11)
# elif rank == 1:
#     data = comm.recv(source=0, tag=11)
#     print("Data received from source {} is {}".format(0, data))


# if rank == 0:
#     data = np.arange(1000, dtype='i')
#     comm.Send([data, MPI.INT], dest=1, tag=77)
# elif rank == 1:
#     data = np.empty(1000, dtype='i')
#     comm.Recv([data, MPI.INT], source=0, tag=77)
#     print(data)

# # automatic MPI datatype discovery
# if rank == 0:
#     data = np.arange(100, dtype=np.float64)
#     comm.Send(data, dest=1, tag=13)
# elif rank == 1:
#     data = np.empty(100, dtype=np.float64)
#     comm.Recv(data, source=0, tag=13)
#     print("Data received from source {} is {}".format(0, data))


# if rank == 0:
#     data = {'key1' : [7, 2.72, 2+3j],
#             'key2' : ( 'abc', 'xyz')}
# else:
#     data = None
# data = comm.bcast(data, root=0)
# print("Data received at node {} from source {} is {}".format(rank, 0, data))



# if rank == 0:
#     data = [(i+1)**2 for i in range(size)]
# else:
#     data = None
# data = comm.scatter(data, root=0)
# print("Data received at node {} from source {} is {}".format(rank, 0, data))


# data = (rank+1)**2
# data = comm.gather(data, root=0)
# if rank == 0:
# 	print("Data gathered at node {} is {}".format(0, data))


# if rank == 0:
#     # data = list(range(100))
#     data = np.arange(100, dtype='i')
# else:
# 	data = None

# self_data = np.empty(25, dtype='i')

# comm.Scatter(data, self_data, root=0)
# print("Data received at node {} from source {} is {}\n".format(rank, 0, self_data))


# sendbuf = None
# if rank == 0:
#     sendbuf = np.empty([size, 100], dtype='i')
#     sendbuf.T[:,:] = range(size)
# recvbuf = np.empty(100, dtype='i')
# comm.Scatter(sendbuf, recvbuf, root=0)
# print("Data received at node {} from source {} is {}".format(rank, 0, sendbuf))


# sendbuf = np.zeros(100, dtype='i') + rank
# recvbuf = None
# if rank == 0:
#     recvbuf = np.empty([size, 100], dtype='i')
# comm.Gather(sendbuf, recvbuf, root=0)
# if rank == 0:
# 	print("Data gathered at node {} is {}".format(0, recvbuf))




from mpi4py import MPI
import numpy
import sys

comm = MPI.COMM_SELF.Spawn(sys.executable, args=['cpi.py'], maxprocs=5)
rank = comm.Get_rank()
size = comm.Get_size()


print("Parent id is {}".format(rank))
N = numpy.array(100, 'i')
comm.Bcast([N, MPI.INT], root=MPI.ROOT)
PI = numpy.array(0.0, 'd')
comm.Reduce(None, [PI, MPI.DOUBLE], op=MPI.SUM, root=MPI.ROOT)
# print(PI)

comm.Disconnect()