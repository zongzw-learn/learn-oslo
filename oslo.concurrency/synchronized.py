# -*- coding: utf-8

from oslo_concurrency import lockutils
import time
import threading
import random

@lockutils.synchronized('test-lock')
def func1(id):
    time.sleep(random.random())
    print("func1 is called. %d" % id)
    time.sleep(random.random())
    print("func1 is over. %d" % id)


for n in xrange(4):
    t = threading.Thread(target=func1, args=(n, ))
    t.setDaemon(True)
    t.start()

time.sleep(5)

@lockutils.synchronized('test-lock')
def func2(id):
    time.sleep(random.random())
    print("func2 is called. %d" % id)
    time.sleep(random.random())
    print("func2 is over. %d" % id)

# at a time, only one of func1 and func2 can be called.

'''
添加前缀以保证不同项目之间的锁不会冲突。

(in nova/utils.py)
from oslo_concurrency import lockutils

synchronized = lockutils.synchronized_with_prefix('nova-')


(in nova/foo.py)
from nova import utils

@utils.synchronized('mylock')
def bar(self, *args):
    ...
'''