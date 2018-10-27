from oslo_config import cfg
from oslo_middleware import sizelimit
from oslo_log import log as logging
from oslo_service import wsgi
from oslo_service import service
import json

CONF = cfg.CONF

LOG = logging.getLogger(__name__)
logging.register_options(CONF)
logging.setup(CONF, "middleware_log")

CONF(['--config-file', 'middleware.conf'])

def app_func(environ, start_response):
    print(type(environ))
    #LOG.info(environ)
    start_response("200 OK",[('Content-type', 'text/html')])
    #return "<p>%s</p>" % json.dumps(environ)
    return "<p>%s</p>" % """
    zongzw
    Andrew Zong
    F5 Networks
    """

app_sizelimit = sizelimit.RequestBodySizeLimiter(app_func)
server = wsgi.Server(CONF, "middleware_server", app_sizelimit, 
                    host='0.0.0.0', port=8585)

launcher = service.ProcessLauncher(CONF)
launcher.launch_service(server)

import time
time.sleep(100)

'''
configuration: 
[oslo_middleware]
max_request_body_size = 10

test: 
curl localhost:8585 -d "1234567890abc"

response: 

<html>
 <head>
  <title>413 Request Entity Too Large</title>
 </head>
 <body>
  <h1>413 Request Entity Too Large</h1>
  Request is too large.<br /><br />



 </body>
</html>
'''


