import multiprocessing as mp
import numpy as np

def process_chunk(chunk):
    return np.sum(chunk ** 2)

if __name__ == "__main__":
    data = np.arange(1000000)
    chunks = np.array_split(data, 4)
    with mp.Pool(processes=4) as pool:
        results = pool.map(process_chunk, chunks)
    total = sum(results)
    print(total)