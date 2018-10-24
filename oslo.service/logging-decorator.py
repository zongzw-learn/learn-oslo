'''
def periodic_task(*args, **kwargs):
    def decorator(f):
        # Test for old style invocation
        if 'ticks_between_runs' in kwargs:
            raise InvalidPeriodicTaskArg(arg='ticks_between_runs')

        # Control if run at all
        f._periodic_task = True
        f._periodic_external_ok = kwargs.pop('external_process_ok', False)
        f._periodic_enabled = kwargs.pop('enabled', True)
        f._periodic_name = kwargs.pop('name', f.__name__)

        # Control frequency
        f._periodic_spacing = kwargs.pop('spacing', 0)
        f._periodic_immediate = kwargs.pop('run_immediately', False)
        if f._periodic_immediate:
            f._periodic_last_run = None
        else:
            f._periodic_last_run = now()
        return f
    if kwargs:
        return decorator
    else:
        return decorator(args[0])
'''

from oslo_log import log
from oslo_config import cfg
from oslo_utils import timeutils

CONF = cfg.CONF

def logging_enabled(*args, **kwargs):
    def decorator(f):
        print("function", f)
        print("args", args)
        print("kwargs", kwargs)

        return f
    
    print("decorator: logging_enabled")

    if kwargs:
        print("kwargs not none")
        return decorator
    else:
        print("kwargs none")
        return decorator(args[0])


@logging_enabled
def myfunc1(a, b, c):
    print(a)
    print(b)
    print(c)

@logging_enabled(name="num", value="23")
def myfunc2(a, b):
    print(a)
    print(b)

#myfunc1(1, 2, 3)
#myfunc2('a', 'b')


def authorized(f):
    def decorator(user, *args):
        if user == 'zong':
            return f(user, *args)
        else:
            def func(user, *args):
                print(user, "not authorized")
            return func(user, *args)
    
    return decorator

@authorized
def dosomething(user, *args):
    print(user, ' done')


print("hello")

dosomething('zong', 'a', 'b')
dosomething('andrew', 'a', 'b')