from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.forms.models import model_to_dict
from django.views.generic import TemplateView,ListView

from .models import Character, Stats
from django.db.models import Q

# Create your views here.
class HomePageView(TemplateView):
    template_name = "chara_search/index.html"

    def dispatch(self, request, *args, **kwargs):
        self.request.session['query'] = None #Clear the session variable when returning to the home page
        template = loader.get_template("chara_search/index.html")
        return HttpResponse(template.render())

def sheet(request, character_id):
    # @TODO Make sheet iterable so I can make the actual static sheet itself one giant for loop
    sheet = Stats.objects.get(character=character_id)
    #print(sheet.character.first_name)
    template = loader.get_template('chara_search/sheet.html')
    context = {
        'sheet': sheet,
    }
    return HttpResponse(template.render(context,request))

class SearchResultsView(ListView):
    model = Character
    template_name = "chara_search/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("display_name")
        #print(query)
        self.request.session['query'] = query
        character_list = Character.objects.filter(
            Q(display_name__contains=query)
        )
        return character_list
