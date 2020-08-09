from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        self.request.session['query'] = None #Clear the session variable when returning to the home page
        template = loader.get_template("index.html")
        return HttpResponse(template.render())