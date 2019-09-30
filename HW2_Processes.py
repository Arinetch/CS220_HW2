import shutil
import os
from concurrent.futures import ProcessPoolExecutor
import time

def task(source, destination):
    files = os.listdir(source)
    for i in files:
        shutil.copy2(source + i, destination)

my_source = '/Users/mac/Desktop/Desktop/AUA/Fall 2019/Parallel HPC/Python HW/untitled folder/'
my_destination = '/Users/mac/Desktop/Desktop/AUA/Fall 2019/Parallel HPC/Python HW/untitled folder 2/'

def main():
    executor = ProcessPoolExecutor(5)
    start = time.time()
    executor.submit(task, my_source, my_destination)
    end = time.time()
    print(end - start)

if __name__ == '__main__':
    main()
