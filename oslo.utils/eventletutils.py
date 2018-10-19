# -*- coding: utf-8 -*-
'''
monkey-patch
dynamically replace modules

green thread
http://eventlet.net/doc/modules/greenthread.html

Or
如果使用线程做过重要的编程，你就知道写出程序有多么困难，因为调度程序任何时候都能中断线程。
必须记住保留锁，去保护程序中的重要部分，防止多步操作在执行的过程中中断，防止数据处于无效状态。
而协程默认会做好全方位保护，以防止中断。我们必须显式产出才能让程序的余下部分运行。
对协程来说，无需保留锁，在多个线程之间同步操作，协程自身就会同步，因为在任意时刻只有一个协程运行。
想交出控制权时，可以使用 yield 或 yield from 把控制权交还调度程序。
这就是能够安全地取消协程的原因：按照定义，协程只能在暂停的 yield处取消，
因此可以处理 CancelledError 异常，执行清理操作。

总而言之，协程比线程更节省资源，效率更高，并且更安全。

'''

from oslo_utils import eventletutils

print(locals())
print(globals())

print(eventletutils.fetch_current_thread_functor())

print(eventletutils.is_monkey_patched('sys'))

eventletutils.warn_eventlet_not_patched(expected_patched_modules=None, what='this library')
