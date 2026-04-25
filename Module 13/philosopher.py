import random
import threading 
import time

from fork import Fork

class Philosopher(threading.Thread):
    running = True

    # initialize a Philosopher's name, left/right fork
    def __init__(self, name: str, left_fork: Fork, right_fork: Fork):
        # call threadiing class superclass constructor
        threading.Thread.__init__(self)
        # initialize name instance variable 
        self.name = name 
        # initialize left fork instance variable 
        self.left_fork = left_fork
        # initialize right forl instance variable 
        self.right_fork = right_fork

    # run () is called by thread's start () method, starts the thread running
    def run(self):
        while self.running:
            # call think()
            self.think()
            # call eat()
            self.eat()
        # print <philosopher name> is cleaning up 
        print(self.name + " is cleaning up.")

    # make philosophwer think for a random number of seconds until hungry
    def think(self):
        # thinking = random number of seconds between 3 and 5 ysing random.uniform(0)
        thinking = random.uniform(3, 5)
        # print <philosopher name> is thinking for thinking seconds
        print(self.name + " is thinking for " + str(thinking) + " seconds.")
        # sleep for thinking seconds 
        time.sleep(thinking)
        # print <philosopher name> is now hungry
        print(self.name + " is now hungry.")

    # make philosopher eat for a random number of seconds until thinking again
    def eat(self):
        # try to acquire left fork
        if self.left_fork.acquire_fork():
            # if successful, try to acquie right fork
            if self.right_fork.acquire_fork():
                # if successful 
                # eating = random number of seconds between 3 and 5 using random.uniform()
                eating = random.uniform(3, 5)
                # print <philosopher name> is eating for eating seconds.
                print(self.name + " is eating for " + str(eating) + " seconds.")
                # sleep for eating seconds
                time.sleep(eating)

                # release right fork 
                self.right_fork.release_fork()
                # print <philosopher name> has put down his right fork.
                print(self.name + " has put down his right fork.")

            # release left fork
            self.left_fork.release_fork()
            # print <philosopher name> has put down hus left fork.
            print(self.name + " has put down his left fork.")

        # else: return
        else:
            return 