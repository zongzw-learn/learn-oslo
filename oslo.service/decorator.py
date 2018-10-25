# -*- coding: utf-8 -*-
from oslo_log import log
from oslo_config import cfg
from oslo_utils import timeutils

CONF = cfg.CONF

'''
decorator without parameters
'''

'''
@authorize decorator
'''
def authorize(f):
    def decorator(user, *args):
        if user == 'zong':
            return f(user, *args)
        else:
            def func(user, *args):
                print(user, "not authorized")
            return func(user, *args)
    
    return decorator

'''
@logfunc
'''
def logfunc(f):
    def decorator(*args, **kwargs):
        print("log function ", f.__name__)
        print("log args ", args)
        print("log kwargs ", kwargs)
        return f(*args, **kwargs)

    return decorator

@authorize
def work1(user, *args):
    print(user, ' done')

@logfunc
def work2(username, password):
    print("work2 called, username: ", username, "password: ", password)

@logfunc
def work3(param, *args, **kwargs):
    print("work3 called, param: ", 
        param, "args: %s, kwargs: %s" % (args, kwargs))

@authorize
@logfunc
def work4(user, p1, p2, p3):
    print(user, p1, p2, p3)

print("hello")

print("===========================")
work1('zong', 'a', 'b')
print("===========================")
work1('andrew', 'a', 'b')
print("===========================")
work2("andrew", "zongzw")
print("===========================")
work3("I", 'want', 'to', 'run', where="park", when="saturday")
print("===========================")
work4('zong', '1', '2', 3)
print("===========================")

'''
decorator with parameters
'''
print("---------------------------")
def mydecorator(*args, **kwargs):
    def decorator(f):
        print("dparams: ", f)
        print("params: ", args, kwargs)

        return f

    return decorator

print("---------------------------")
@mydecorator('a', 2, x=23)
def func1():
    print('func1')

print("---------------------------")
func1()

print("---------------------------")
@mydecorator('b', 3, x=24)
def func2(*args, **kwargs):
    print("func2", args, kwargs)

print("---------------------------")
func2(1, 2)

print("---------------------------")
func2(2, 3, 'x', x=4)

'''
没有参数的decorator和有参数的decorator在实现上不同。 

没有参数的decorator 
* 传入的参数是 f，
* 其中的wrapper以被装饰的函数的参数为参数。
* 在被装饰函数被调用时触发调用。

有参数的decorator
* 传入的参数 是被装饰函数的参数
* 其中的wrapper的参数是f。
* 在被装饰函数被定义时调用。
'''
