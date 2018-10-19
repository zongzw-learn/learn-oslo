from oslo_utils import secretutils

print(secretutils.constant_time_compare('a', 'a'))
print(secretutils.constant_time_compare('a', 'b'))
print(secretutils.constant_time_compare('a', 'ab'))

print(secretutils.constant_time_compare(b'a', b'a'))
print(secretutils.constant_time_compare(b'a', b'b'))
print(secretutils.constant_time_compare(b'a', b'ab'))