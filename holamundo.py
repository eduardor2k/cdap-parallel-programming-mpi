#!/usr/bin/env python
from mpi4py import MPI
comm = MPI.COMM_WORLD
print "Hola! Soy el proceso %d de %d!" % (comm.rank, comm.size)
comm.Barrier() # Barrera
