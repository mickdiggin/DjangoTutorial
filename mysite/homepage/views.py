from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

class MainView(generic.ListView):
    template_name = "homepage/index.html"
    greeting = "Good Day"

    def get(self, request):
        return HttpResponse(self.template_name)