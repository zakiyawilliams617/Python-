import time 

from fork import Fork
from philosopher import Philosopher 

def DiningPhilosophers():
    # create array of 5 names: Plato, Aristotle, Buddha, Marx, and Nietzsche
    names = ["Plato", "Aristotle", "Buddha", "Marx", "Nietzsche"]

    # create 5 forks
    forks = [Fork() for i in range(5)]

    # create 5 philosphers and correctly assign each pair of forks to each philosopher
    # philosopher i gets fork i (left) and fork (i+1) %b 5 (right)
    philosophers = [Philosopher(names[i], forks[i], forks[(i + 1) % 5]) for i in range(5)]

    # start all 5 philosooher threads, shold be non blocking 
    for philosopher in philosophers:
        philosopher.start()

    # sleep for 10 seconds
    time.sleep(10)

    # set running to false
    Philosopher.running = False

    # exit all threads
    for philosopher in philosophers:
        philosopher.join()

if __name__ == "__main__":
    DiningPhilosophers()