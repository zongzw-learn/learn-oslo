from oslo_service import sslutils
from oslo_config import cfg

'''
oslo-config-generator --namespace oslo.service.sslutils
'''

CONF = cfg.CONF
CONF(['--config-file', 'sslutils.conf'])

sslutils.is_enabled(CONF)
