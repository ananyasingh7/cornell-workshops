import concurrent.futures
import time

def task1():
    time.sleep(1)
    return "Task 1 done"

def task2():
    time.sleep(2)
    return "Task 2 done"

def task3(dep1, dep2):
    return f"Task 3 done with {dep1} and {dep2}"

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future1 = executor.submit(task1)
        future2 = executor.submit(task2)
        result1 = future1.result()
        result2 = future2.result()
        future3 = executor.submit(task3, result1, result2)
        result3 = future3.result()
    print(result3)