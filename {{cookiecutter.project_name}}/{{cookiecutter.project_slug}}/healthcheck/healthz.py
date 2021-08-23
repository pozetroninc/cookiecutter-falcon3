# Third-party imports
import falcon


class HealthCheck(object):
    """ A Simple HealthCheck which returns 200 OK
    """

    @staticmethod
    def on_get(req, resp):
        resp.status = falcon.HTTP_200
        resp.text = 'GOOD'


class AsyncHealthCheck:
    """ A Simple HealthCheck which returns 200 OK
    """

    @staticmethod
    async def on_get(req, resp):
        resp.status = falcon.HTTP_200
        resp.text = 'GOOD'