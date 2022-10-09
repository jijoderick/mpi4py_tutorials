from mpi4py import MPI
import numpy
sendbuf = []
comm = MPI.COMM_WORLD
if comm.rank == 0:
    m= numpy.random.randn(comm.size, comm.size)
    print("Original array on rank 0:\n" + str(m))
    sendbuf = m
v= comm.scatter(sendbuf, root = 0)
print("Rank "+str(comm.rank)+"I got this array:\n" + str(v))
v = v*v
recvbuf = comm.gather(v, root = 0)
if comm.rank == 0:
    print("New array on rank 0:\n"+ str(numpy.array(recvbuf)))
if MPI.COMM_WORLD.rank == 0:
    sendbuf = "Done!"
recv =MPI.COMM_WORLD.bcast(sendbuf, root = 0)
recv2= MPI.COMM_WORLD.bcast(recvbuf, root = 0)
print("My rank is "+str(comm.rank)+",From root,  I received the message "+recv+"\n the following array " +str(recv2))
