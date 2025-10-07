import multiprocessing as mp

def square(x):
    return x * x

if __name__ == "__main__":
    data = list(range(10))
    with mp.Pool(processes=4) as pool:
        results = pool.map(square, data)
    print(results)