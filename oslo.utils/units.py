from oslo_utils import units
from oslo_utils import reflection

for n in reflection.get_members(units):
    print("%s: %s" % (reflection.get_callable_name(n), n))

print(units.E)
