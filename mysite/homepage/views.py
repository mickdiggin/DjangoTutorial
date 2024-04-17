from django.http import HttpResponse
from django.views import generic


class MainView(generic.ListView):
    template_name = "homepage/index.html"
    greeting = "Good Day"

    def get(self, request):
        return HttpResponse(self.template_name)
