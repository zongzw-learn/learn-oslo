from oslo_service import service
from oslo_service import wsgi

from oslo_config import cfg
from oslo_utils import uuidutils
from oslo_utils import timeutils

import sys
import time

'''
Using oslo.service with oslo-config-generator¶

The oslo.service provides several entry points to generate a configuration files.

    oslo.service.service
        The options from the service and eventlet_backdoor modules for the [DEFAULT] section.

    oslo.service.periodic_task
        The options from the periodic_task module for the [DEFAULT] section.

    oslo.service.sslutils
        The options from the sslutils module for the [ssl] section.

    oslo.service.wsgi
        The options from the wsgi module for the [DEFAULT] section.


'''
class SampleService(service.Service):
    def __init__(self):
        self.id = uuidutils.generate_uuid()
        super(SampleService, self).__init__()

    def reset(self):
        print("%s: %s reset is called." % (timeutils.strtime(), self.id))
        time.sleep(0.2)
    
    def start(self):
        print("%s: %s start is called." % (timeutils.strtime(), self.id))
        time.sleep(0.2)

    def stop(self):
        print("%s: %s stop is called." % (timeutils.strtime(), self.id))
        time.sleep(0.2)

    def wait(self):
        print("%s: %s wait is called." % (timeutils.strtime(), self.id))
        time.sleep(0.2)

from oslo_config import cfg
from oslo_service import service

CONF = cfg.CONF

print("=====================================")
service_launcher = service.ServiceLauncher(CONF)
service_launcher.launch_service(SampleService())

print("=====================================")
process_launcher = service.ProcessLauncher(CONF, wait_interval=1.0)
process_launcher.launch_service(service.Service(), workers=2)

print("=====================================")
launcher = service.launch(CONF, SampleService(), workers=3)
