'''
need to install:
    pip install fixtures

or it reports: 
    ImportError: No module named fixtures
'''

from oslo_utils import fixture
from oslo_utils import timeutils
import time

print(timeutils.utcnow.override_time)
with fixture.TimeFixture():
    print(timeutils.utcnow.override_time)
    time.sleep(1)
    print(timeutils.utcnow.override_time)
    
print(timeutils.utcnow.override_time)
