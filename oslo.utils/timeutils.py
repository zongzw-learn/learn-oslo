from oslo_utils import timeutils

'''
all functions: 
    w.elapsed
    w.expired
    w.has_started
    w.has_stopped
    w.leftover
    w.restart
    w.resume
    w.split
    w.splits
    w.start
    w.stop
'''

import time

def slow_routine(delay):
    def i_am_slow():
        time.sleep(delay)
    return i_am_slow

func = slow_routine(0.5)

with timeutils.StopWatch() as w: # implicitely called w.stop()
    func()

print(w.elapsed())

w = timeutils.StopWatch(duration=1)
w.start()

w.split()
time.sleep(0.1)
w.split()
print(w.splits)

time.sleep(0.6)
print(w.elapsed())
print(w.leftover())

time.sleep(0.5)
print(w.expired())

'''
0.502276873915
(Split(elapsed=1.33761204779e-05, length=1.33761204779e-05), Split(elapsed=0.103919066023, length=0.103905689903))
0.704424031079
0.295529895928
True
'''