from oslo_concurrency import watchdog
import subprocess
import logging

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT)
LOG = logging.getLogger('mylogger')

with watchdog.watch(LOG, "subprocess call", logging.ERROR, after=2):
    subprocess.call("sleep 3", shell=True)
    print "done"
