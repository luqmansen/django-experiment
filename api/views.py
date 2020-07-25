import logging

import pyfiglet
from django.conf import settings
from django.http import HttpResponse
from django.views import View
from opentracing_instrumentation import span_in_context, get_current_span

logger = logging.getLogger('api.views')

tracer = settings.TRACER
# print(tracer.reporter.reporters[0]._channel.local_agent_http.__dict__)


class BaseClasss(View):

    def __repr__(self):
        return str(self.__class__.__name__)


class YeetView(BaseClasss):
    """Generate 1000 Yeet
    Example of using tracer on class based view
    TODO: create decorator to wrap views method
    """

    def get(self, request, *args, **kwargs):
        with tracer.start_span(self) as span:
            with span_in_context(span):
                yeet = self.yeet_generator()
                return HttpResponse(yeet, content_type='text/plain')

    def yeet_generator(self):
        with tracer.start_span("yeet_gen_1", child_of=get_current_span()) as span:
            with span_in_context(span):
                y = [pyfiglet.figlet_format("Yeet!!") for _ in range(1000)]
                x = self.yeet_gen_2()
                x.append(y)
                return y

    @staticmethod
    def yeet_gen_2():
        with tracer.start_span("yeet_gen_2", child_of=get_current_span()) as span:
            with span_in_context(span):
                y = pyfiglet.figlet_format("Yeet!!")
                return [y for _ in range(10000)]
