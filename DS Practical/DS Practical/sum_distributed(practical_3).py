from mpi4py import MPI
import numpy as np

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Master process initializes data
if rank == 0:
    N = 16  # Total number of elements
    data = np.arange(1, N + 1)
    print(f"Original array: {data}")

    # Pad data if not divisible by number of processors
    if N % size != 0:
        pad_size = size - (N % size)
        data = np.pad(data, (0, pad_size), mode='constant')
    
    chunks = np.array_split(data, size)
else:
    chunks = None

# Scatter the data
local_data = comm.scatter(chunks, root=0)

# Each processor computes its local sum
local_sum = np.sum(local_data)
print(f"Processor {rank}: received {local_data}, local sum = {local_sum}")

# Gather the local sums to the master
all_sums = comm.gather(local_sum, root=0)

# Final sum calculation at master
if rank == 0:
    total_sum = sum(all_sums)
    print(f"\nIntermediate sums from all processors: {all_sums}")
    print(f"Final total sum: {total_sum}")
