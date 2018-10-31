from oslo_concurrency import lockutils
from oslo_utils import timeutils

import time
import random
import threading

rwlock = lockutils.ReaderWriterLock()

cache = []
index = 0
dur = 10
def push():
    global index 
    global rwlock
    with timeutils.StopWatch(duration=dur) as w:
        while not w.expired():
            with rwlock.write_lock() as l: 
                num = index
                index += 1

                print("pushing start: %d" % num)
                time.sleep(random.random())
                cache.append(num)
                time.sleep(random.random())
                print("pushing over : %d" % num)

            time.sleep(1)

def pop():
    n = 0
    global rwlock
    with timeutils.StopWatch(duration=dur) as w:
        while not w.expired():
            with rwlock.write_lock() as l: 
                print("poping start :")
                time.sleep(random.random())
                n = cache.pop() if len(cache) else -1
                time.sleep(random.random())
                print("poping over  : %d" % n)

            time.sleep(1)

def read(id):
    global rwlock
    with timeutils.StopWatch(duration=dur) as w:
        while not w.expired():
            with rwlock.read_lock() as l: 
                print("%d reading start:" % id)
                time.sleep(1+random.random())
                n = cache[-1] if len(cache) else -1
                time.sleep(1+random.random())
                print("%d reading over : %d" %(id, n))

            time.sleep(1)

threading.Thread(target=push).start()
threading.Thread(target=pop).start()

for n in xrange(4):
    threading.Thread(target=read, args=(n, )).start()

'''
 pushing start: 0        | pushing start: 0
 poping start :          | pushing over : 0
 0 reading start:        | 0 reading start:
 1 reading start:        | 2 reading start:
 2 reading start:        | 3 reading start:
 3 reading start:        | 1 reading start:
                         | 2 reading over : 0
 pushing over : 0        | 1 reading over : 0
 poping over  : 0        | 0 reading over : 0
 pushing start: 1        | 3 reading over : 0
 poping start :          | poping start :
 3 reading over : -1     | poping over  : 0
 pushing over : 1        | 0 reading start:
 poping over  : 1        | 1 reading start:
 0 reading over : -1     | 3 reading start:2 reading start:
 3 reading start:        |
 2 reading over : -1     | 3 reading over : -1
 1 reading over : -1     | 2 reading over : -1
 pushing start: 2        | 0 reading over : -1
 poping start :          | 1 reading over : -1
 0 reading start:        | pushing start: 1
 2 reading start:        | pushing over : 1
 1 reading start:        | poping start :
 poping over  : -1       | poping over  : 1
 pushing over : 2        | 0 reading start:
 poping start :          | 3 reading start:
 pushing start: 3        | 2 reading start:
 3 reading over : 2      | 0 reading over : -1
 pushing over : 3        | 2 reading over : -1
 poping over  : 2        | 3 reading over : -1
0 reading over : 2
1 reading over : 2
2 reading over : 2
3 reading start:
pushing start: 4
poping start :
0 reading start:
1 reading start:
2 reading start:
pushing over : 4
poping over  : 4
pushing start: 5
pushing over : 5
1 reading over : 3
2 reading over : 3
3 reading over : 5
0 reading over : 5
'''
