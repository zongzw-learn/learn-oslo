from oslo_utils import excutils

@excutils.exception_filter
def ignore_test_exception(ex):
    return isinstance(ex, AssertionError) and 'test' in str(ex)

try:
    assert False, "this is a test"
except Exception as e:
    ignore_test_exception(e)

try:
    assert False, "this is a game"
except Exception as e:
    ignore_test_exception(e)
