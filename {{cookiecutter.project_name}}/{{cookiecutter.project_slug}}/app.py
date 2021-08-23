# -*- coding: utf-8 -*-
"""
App runner
"""
# System imports
from __future__ import absolute_import
# Third-party imports
import falcon

# Local imports
try:
    from sample.models import SampleResource
    from sample.websocket import SampleWebsocket  # pragma: nocover
    from healthcheck.healthz import HealthCheck  # pragma: nocover
    from healthcheck.healthz import AsyncHealthCheck  # pragma: nocover
except ImportError:
    from {{ cookiecutter.project_slug }}.sample.models import SampleResource
    from {{ cookiecutter.project_slug }}.sample.websocket import SampleWebsocket
    from {{ cookiecutter.project_slug }}.healthcheck.healthz import HealthCheck
    from test_falcon3.healthcheck.healthz import AsyncHealthCheck


# Create resources
sample_resource = SampleResource()
sample_websocket = SampleWebsocket()
health_check = HealthCheck()
async_health_check = AsyncHealthCheck()

# Create falcon wsgi app
wsgi_app = falcon.App()
wsgi_app.req_options.strip_url_path_trailing_slash = True
wsgi_app.add_route('/healthz', health_check)
wsgi_app.add_route('/sample_resource', sample_resource)

# Create falcon asgi app
asgi_app = falcon.asgi.App()
asgi_app.req_options.strip_url_path_trailing_slash = True
asgi_app.add_route('/healthz', async_health_check)
asgi_app.add_route('/ws/{example_param}', sample_websocket)


# Useful for debugging problems in API, it works with pdb
if __name__ == '__main__':
    from wsgiref import simple_server  # NOQA
    httpd = simple_server.make_server('127.0.0.1', 8000, wsgi_app)
    httpd.serve_forever()
