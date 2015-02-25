from mpi4py import MPI
import numpy
comm = MPI.COMM_WORLD
sendbuf=[]
root=0
if comm.rank==0:
    m=numpy.array(range(comm.size*comm.size),dtype=float)
    m.shape=(comm.size,comm.size)
    print(m)
    sendbuf=m

v=comm.scatter(sendbuf,root)
print "Datos: %s" % (v) 
v=v*v
recvbuf=comm.gather(v,root)
if comm.rank==0:
    print numpy.array(recvbuf)
