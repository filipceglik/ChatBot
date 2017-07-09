from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    my_dictionary = {'insert_me': "Hello I am from views.py"}
    return render(request, 'index.html', context=my_dictionary)

def chatbotview(SiteView):
    my_dict = {'example': "Chat with bot!"}
    return render(SiteView, 'app.html', context=my_dict)
