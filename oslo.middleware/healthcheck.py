'''
Healthcheck application used for monitoring.

It will respond 200 with “OK” as the body. Or a 503 with the reason as the body if one of the backends reports an application issue.

This is useful for the following reasons:

    Load balancers can ‘ping’ this url to determine service availability.
    Provides an endpoint that is similar to ‘mod_status’ in apache which can provide details (or no details, depending on if configured) about the activity of the server.
    (and more)

'''


'''
curl -i -X HEAD "http://0.0.0.0:8585/healtshcheck"

however, the healthcheck implementation should be done by self.
'''