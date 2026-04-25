import threading

class Fork:
    def __init__(self):
        # add a lock as as instance variable
        self.lock = threading.Lock()

    def acquire_fork(self):
        # return  true if acquire self.lock, false otherwise
        return self.lock.acquire(blocking=False)
    
    def release_fork(self):
        # release lock
        self.lock.release()