#

import time, threading

'''
sta = time.perf_counter()
def a():
    print('start')
    time.sleep(1)
    print('end...')

a()
a() 
end = time.perf_counter()
print(f'finished after {round(end-sta)} second')
'''

# create threading
'''
sta = time.perf_counter()
def a():
    print('start')
    time.sleep(1)
    print('end...')

t = threading.Thread(target=a)  # create the thread
t.start()   # start the thread, not linked with the script thread
t.join()    # linked it with the script thread



end = time.perf_counter()
print(f'finished after {round(end-sta, 4)} second')
'''


'''
sta = time.perf_counter()
def a(b):
    print(f'start, sleeping for {b} second')
    time.sleep(b)
    print('end...')

arr = []
for i in range(10):
    t = threading.Thread(target=a, args=[1.5])  # create the thread
    t.start()   # start the thread, not linked with the script thread
    arr.append(t)
for t in arr:
    t.join()    # linked it with the script thread




end = time.perf_counter()
print(f'finished after {round(end-sta, 4)} second')
'''


import concurrent.futures

'''def a(b):
    print(f'start, sleeping for {b} second')
    time.sleep(b)
    return f'end after {b} second...'

with concurrent.futures.ThreadPoolExecutor() as e:
    times = [5, 3, 4, 1, 2]
    arr = []
    for t in times:
        arr.append(e.submit(a, t))
    for f in concurrent.futures.as_completed(arr):
        print(f.result())'''

