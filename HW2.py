import shutil
import os
import time

def task(source, destination):
    files = os.listdir(source)
    for i in files:
        shutil.copy2(source + i, destination)

my_source = '/Users/mac/Desktop/Desktop/AUA/Fall 2019/Parallel HPC/Python HW/untitled folder/'
my_destination = '/Users/mac/Desktop/Desktop/AUA/Fall 2019/Parallel HPC/Python HW/untitled folder 2/'

def main():
    start = time.time()
    task(my_source, my_destination)
    end = time.time()
    print(end - start)

if __name__ == '__main__':
    main()

# The (end - start) shows that the speed of copying all files from one directory to the other
# without threading and processing is 0.0017461776733398438