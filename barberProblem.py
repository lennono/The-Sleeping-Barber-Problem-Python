import threading
import time
import random
from multiprocessing import Process, Queue, cpu_count
# Not a fair solution will need to use a queue
# Stupid python
#barberReady = threading.Semaphore(value=3)
#customerReady = threading.Semaphore(value=0)
#numberOfFreeSeats = 10 # Atomic variable

def barber(queue):
    while True:
        queue.get()
        #customerReady.acquire()
        print("Barber ")
        #numberOfFreeSeats += 1
        #barberReady.release()
        time.sleep(random.randint(2, 17)) # Hair cut time

def customer(queue):
    queue.put('Work')

    print("customer")
        


class Manager:
    def __init__(self):
        self.queue = Queue()
        self.NUMBER_OF_PROCESSES = cpu_count()

    def start(self):
        self.workers = [Process(target=customer, args=(self.queue,)) for i in range(self.NUMBER_OF_PROCESSES)]
        for w in self.workers:
            w.start()

        barber(self.queue)

    def stop(self):
        self.queue.put(None)
        for i in range(self.NUMBER_OF_PROCESS):
            self.workers[i].join()
        self.queue.close()


Manager().start()