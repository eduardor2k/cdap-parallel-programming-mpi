from mpi4py import MPI
import numpy
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

pases_max = 500
puntos = numpy.zeros(1, dtype = numpy.int)

while puntos[0] < pases_max:
	if rank == 0:
		puntos[0] += 1
		print "%d de %d >>>>" % (puntos,pases_max)
		time.sleep(1)
		comm.Send(puntos, dest=1)
	elif rank == 1:
		print "%d de %d <<<<" % (puntos+1,pases_max)
		time.sleep(1)
		comm.Recv(puntos, source=0)
MPI.Finalize()
