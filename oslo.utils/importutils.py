from oslo_utils import importutils
from oslo_utils import timeutils

import time

first = importutils.import_any('noexists', 'sys')
print(dir(first))

dt = importutils.import_class('datetime.datetime')
print(dir(dt))

ob = importutils.import_object('oslo_config.types.Port', min=443)
print(ob.min)

with importutils.import_object_ns('oslo_utils', 'fixture.TimeFixture'):
    print(timeutils.utcnow.override_time)
    time.sleep(1)
    print(timeutils.utcnow.override_time)

imported = importutils.try_import("abcdef", default='sys')
print(imported)