from oslo_utils import reflection

def args_func(*args):
    print(args)

def kwargs_func(param, *args, **kwargs):
    print(param)
    print(args)
    print(kwargs)

kwargs_func('0', 1, 2, 3, 4, k1=5, k2=6)

class A(object):
    pass

class B(A):
    pass

class C(B):
    pass

for m in [reflection.get_callable_args, reflection.get_callable_name, reflection.accepts_kwargs]:
    for n in [args_func, kwargs_func]:
        print("%-50s (%-20s): %s" % (reflection.get_callable_name(m), reflection.get_callable_name(n), m(n)))

print(list(reflection.get_all_class_names(C())))

# Special arguments (like *args and **kwargs) are not included into output.
#print(reflection.get_callable_args(args_func))
#print(reflection.get_callable_args(kwargs_func))
