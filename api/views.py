import pyfiglet
from django.http import HttpResponse
from django.views import View


class YeetView(View):
    """Generate 1000 Yeet"""
    def get(self, *args, **kwargs):
        y = pyfiglet.figlet_format("Yeet!!")
        l = [y for _ in range(1000)]
        return HttpResponse(l, content_type='text/plain')
