import threading
import time
import random
import Queue
# Not a fair solution will need to use a queue
# Stupid python
barberReady = threading.Semaphore(value=3)
customerReady = threading.Semaphore(value=0)
numberOfFreeSeats = 10 # Atomic variable
customerQueue = Queue.Queue()

def barber():
    global numberOfFreeSeats
    while True:
        customerReady.acquire()
        print "Barber ", threading.current_thread().name
        numberOfFreeSeats += 1
        barberReady.release()
        time.sleep(random.randint(2, 17)) # Hair cut time

def Customer():
        global numberOfFreeSeats

        numberOfFreeSeats -= 1
        customerReady.release() # Customer ready to have a haircut
        barberReady.acquire() #
        print "customer ", threading.current_thread().name  
            


for x in range(3):
    barberOpensUp = threading.Thread(target = barber) 
    barberOpensUp.start() 

while True:

    time.sleep(random.randint(0, 3)) # Wait for next customer
    global numberOfFreeSeats
    #crack
    # Customer leaves if there is no free seat
    if numberOfFreeSeats > 0:  
        nextCustomer = threading.Thread(target = Customer)
        nextCustomer.start()
