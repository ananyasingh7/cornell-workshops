import multiprocessing as mp
import time

def stage1(x):
    return x * 2

def stage2(x):
    return x + 1

def stage3(x):
    return x ** 2

if __name__ == "__main__":
    data = list(range(5))
    with mp.Pool() as pool:
        res1 = pool.map(stage1, data)
        res2 = pool.map(stage2, res1)
        res3 = pool.map(stage3, res2)
    print(res3)