import logging

from django.http import HttpResponse, HttpResponseServerError
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger("healthz")


class HealthCheckMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.method == "GET":
            if request.path == "/readyz":
                return self.readyz()
            elif request.path == "/healthz":
                return self.heatlhz()

    @staticmethod
    def heatlhz():
        return HttpResponse("OK")

    @staticmethod
    def readyz():
        try:
            from django.db import connections
            for name in connections:
                cursor = connections[name].cursor()
                row = cursor.execute("SELECT 1;").fetchone()
                if row is None:
                    return HttpResponseServerError("db invalid response")
        except Exception as e:
            logger.exception(str(e))
            return HttpResponseServerError("db: cannot connect to database")

        return HttpResponse("OK")
