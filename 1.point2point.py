from mpi4py import MPI
import numpy
comm=MPI.COMM_WORLD
rank=comm.rank
size=comm.size
v=numpy.array([rank]*10, dtype=float)
if comm.rank == 0:
    comm.send(v, dest = (rank+1)%size)
if comm.rank > 0:
    data = comm.recv(source = (rank-1)%size)
    comm.send(v, dest = (rank+1)%size)
if comm.rank == 0:
    data = comm.recv(source = size -1)
print("My rank is "+ str(rank)+"\n I received this:\n"+ str(data))
