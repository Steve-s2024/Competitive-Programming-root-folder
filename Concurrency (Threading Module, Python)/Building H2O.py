


# TLE
from threading import Semaphore, Lock

class H2O:
    def __init__(self):
        self.os = Semaphore(0)
        self.hs = Semaphore(0)
        self.l = Lock()
        self.l.acquire()
        self.h = 0

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h += 1
        if self.h >= 2:
            self.h -= 2
            self.os.acquire()
            # releaseHydrogen() outputs "H". Do not change or remove this line.
            releaseHydrogen()
            releaseHydrogen()
            self.l.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.os.release()
        self.l.acquire()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()