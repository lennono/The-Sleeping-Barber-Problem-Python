import threading
import time
import random
from multiprocessing import Process, Queue, cpu_count


def barber(queue):
    while True:
        queue.get()
        print("Barber ")
        time.sleep(random.randint(2, 17)) # Hair cut time

def customer(queue):
    queue.put('Work')
    print("customer")
    # Can put up a while loop here to mimic a continuous stream of customers
        


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