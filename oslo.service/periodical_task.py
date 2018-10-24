from oslo_service import periodic_task
from oslo_utils import timeutils
from oslo_config import cfg

from oslo_service import service

import time

class PService(periodic_task.PeriodicTasks):
    @periodic_task.periodic_task(spacing=3, run_immediately=True, name="testprocess")
    def func(self, context):
        print("func: %s, running" % timeutils.strtime())
    
CONF = cfg.CONF

@periodic_task.periodic_task(run_immediately=True, name='addedprocess')
def foo(self, context):
    print("%s: %s, running" % ('foo', timeutils.strtime()))


@periodic_task.periodic_task(spacing=5, run_immediately=True, name='appendedprocess')
def bar(self, context):
    print("%s: %s, running" % ('bar', timeutils.strtime()))

ps = PService(CONF)
ps.add_periodic_task(foo)
ps.add_periodic_task(bar)

while True: 
    ps.run_periodic_tasks(None)
    time.sleep(0.1)
