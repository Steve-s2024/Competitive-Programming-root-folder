# make a bit slower but easier to read: 34%
import threading


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.cnt = 1
        self.l = threading.Lock()
        self.lEven = threading.Lock()
        self.lOdd = threading.Lock()
        self.l.acquire()
        self.lEven.acquire()
        self.lOdd.acquire()

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            printNumber(0)
            self.lOdd.release()
            self.l.acquire()
            if self.cnt > self.n:
                break
            printNumber(0)
            self.lEven.release()
            self.l.acquire()
            if self.cnt > self.n:
                break
        self.lEven.release()
        self.lOdd.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            self.lEven.acquire()
            if self.cnt > self.n:
                break
            printNumber(self.cnt)
            self.cnt += 1
            self.l.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            self.lOdd.acquire()
            if self.cnt > self.n:
                break
            printNumber(self.cnt)
            self.cnt += 1
            self.l.release()





# didn't work
import threading


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.cnt = 1
        self.l = threading.Lock()
        self.lEven = threading.Lock()
        self.lOdd = threading.Lock()
        self.l.acquire()
        self.lEven.acquire()
        self.lOdd.acquire()

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        while True:

            self.lOdd.release()
            self.l.acquire()
            if self.cnt == self.n:
                break
            self.lEven.release()
            self.l.acquire()
            if self.cnt == self.n:
                break

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        while self.cnt <= self.n:
            self.lEven.acquire()
            printNumber(self.cnt)
            self.cnt += 1
            self.l.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        while self.cnt <= self.n:
            self.lOdd.acquire()
            printNumber(self.cnt)
            self.cnt += 1
            self.l.release()
