# i have to create a new thread called 'a', it contains the main thread which do the iteration from 1 to n, and interact
# with all the rest four threads. I can't just call self.mainThread() in __init__, it will block the call path: 58%

from threading import Lock, Thread

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.l = Lock()
        self.f = Lock()
        self.b = Lock()
        self.fb = Lock()
        self.nu = Lock()
        self.f.acquire()
        self.b.acquire()
        self.fb.acquire()
        self.nu.acquire()
        self.cnt = 1
        a = Thread(target = self.mainThread, args = [])
        a.start()

    def mainThread(self):
        # print('main thread begin')
        for i in range(1, self.n + 1):
            self.l.acquire()
            if i % 15 == 0:
                self.fb.release()
            elif i % 5 == 0:
                self.b.release()
            elif i % 3 == 0:
                self.f.release()
            else:
                self.nu.release()
        # print('main thread end')
        self.l.acquire()
        self.f.release()
        self.b.release()
        self.fb.release()
        self.nu.release()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            self.f.acquire()
            if self.cnt > self.n:
                break
            printFizz()
            self.cnt += 1
            self.l.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while self.cnt + 4 <= self.n:
            self.b.acquire()
            if self.cnt > self.n:
                break
            printBuzz()
            self.cnt += 1
            self.l.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.fb.acquire()
            if self.cnt > self.n:
                break
            printFizzBuzz()
            self.cnt += 1
            self.l.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while self.cnt <= self.n:
            self.nu.acquire()
            if self.cnt > self.n:
                break
            printNumber(self.cnt)
            self.cnt += 1
            self.l.release()




# practice, deprecated
import threading
from threading import Lock
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.l = Lock()
        self.nu = Lock()
        self.nu.acquire()
        self.cnt = 0

    def start(self):
        # print('main thread begin!')
        for i in range(1, self.n + 1):
            # print('main thread')
            self.l.acquire()
            # print('main thread acquired')
            # print('sub thread released')
            self.nu.release()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        return

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        return

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        return

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        # print('sub thread begin!')
        while True:
            self.nu.acquire()
            # print('sub thread acquired')
            self.cnt += 1
            printNumber(self.cnt)
            if self.cnt >= self.n:
                self.l.release()
                break
            # print('main thread released')
            self.l.release()
        # print('sub thread end!')

def printNumber(x):
    print(x)

obj = FizzBuzz(10)
b = threading.Thread(target = obj.start, args = [])
a = threading.Thread(target = obj.number, args = [printNumber])
a.start()
b.start()



