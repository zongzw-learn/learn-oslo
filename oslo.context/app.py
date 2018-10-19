from oslo_config import cfg
from oslo_context import context
from oslo_log import log as logging

CONF = cfg.CONF
DOMAIN = "demo"

logging.register_options(CONF)
logging.setup(CONF, DOMAIN)

LOG = logging.getLogger(__name__)

LOG.info("Message without context")
context.RequestContext()
LOG.info("Message with context")

'''
he oslo.context variables used in the logging_context_format_string and logging_user_identity_format configuration options include:

    global_request_id - A request id (e.g. req-9f2c484a-b504-4fd9-b44c-4357544cca50) which may have been sent in from another service to indicate this is part of a chain of requests.
    request_id - A request id (e.g. req-9f2c484a-b504-4fd9-b44c-4357544cca50)
    user - A user id (e.g. e5bc7033e6b7473c9fe8ee1bd4df79a3)
    tenant - A tenant/project id (e.g. 79e338475db84f7c91ee4e86b79b34c1)
    domain - A domain id
    user_domain - A user domain id
    project_domain - A project domain id

'''

ctx = context.RequestContext(user_id='6ce90b4d',
                       project_id='d6134462',
                       project_domain_id='a6b9360e')


LOG.info("Message with context")
LOG.info("Message with passed context", context=ctx)

print(CONF.logging_user_identity_format)
print(CONF.logging_context_format_string)
CONF.logging_user_identity_format = "%(user)s/%(tenant)s@%(project_domain)s"

LOG.info("Message with passed context", context=ctx)
