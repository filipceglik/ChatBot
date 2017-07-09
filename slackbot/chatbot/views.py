from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import JsonResponse
from django.views.generic.base import TemplateView
# Create your views here.
def index(request):
    my_dictionary = {'insert_me': "Hello I am from views.py"}
    return render(request, 'index.html', context=my_dictionary)

def chatbotview(SiteView):
    my_dict = {'example': "Chat with bot!"}
    return render(SiteView, 'app.html', context=my_dict)

class ChatterBotAppView(TemplateView):
    template_name = "app1.html"
