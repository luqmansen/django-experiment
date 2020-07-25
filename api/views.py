from time import time

from django.http import JsonResponse, HttpResponse
from django.views import View
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary, Counter, Histogram, Gauge, generate_latest

_INF = float("inf")

graphs = {}
graphs["c"] = Counter("python_get_request_ops_total", 'Total Request for GET request')
graphs["h"] = Histogram("python_request_duration_second", 'Histogram for duration', buckets=(1, 2, 5, 6, 10, _INF))


class Yeet(View):
    """Generate 100 Yeet"""

    def get(self, *args, **kwargs):
        start = time()
        graphs["c"].inc()
        yeet = ["Yeet" for _ in range(100)]
        end = time()
        graphs["h"].observe(end - start)
        return JsonResponse(yeet, safe=False)


class Metrics(View):
    def get(self, *args, **kwargs):
        res = list()
        for k, v in graphs.items():
            res.append(generate_latest(v))
        return HttpResponse(res, content_type='text/plain')
