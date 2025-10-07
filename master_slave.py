import multiprocessing as mp
import time

def worker(task):
    time.sleep(1)
    return f"Processed {task}"

if __name__ == "__main__":
    tasks = [1, 2, 3, 4, 5]
    with mp.Pool(processes=3) as pool:  # Master creates pool of slaves
        results = pool.map(worker, tasks)
    print(results)