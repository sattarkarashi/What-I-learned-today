import threading
import multiprocessing

'''Threading and multiprocessing are used for CPU intensive tasks normally.'''

def big_task():
    print("Starting big task")
    x = 0
    for i in range(10000):
        for j in range(10000 ):
            x += i*j
    
    print(x)
    print("Ending big task")


print("Starting main program")
th = threading.Thread(target=big_task)
th.start()

pr = multiprocessing.Process(target=big_task)
pr.start()
print("Ending main program")