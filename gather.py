from mpi4py import MPI
import numpy
sendbuf = []
comm = MPI.COMM_WORLD
if comm.rank == 0:
    m= numpy.random.randn(comm.size, comm.size)
    print("Original array on rank 0:\n" + str(m))
    sendbuf = m
v= comm.scatter(sendbuf, root = 0)
print("I got this array:\n" + str(v))
v = v*v
recvbuf = comm.gather(v, root = 0)
if comm.rank == 0:
    print("New array on rank 0:\n"+ str(numpy.array(recvbuf)))
