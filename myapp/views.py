import facebook
import random
from django.shortcuts import render
from django_facebook.decorators import canvas_only

QUOTES = [
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
]

@canvas_only
def home(request):
    me = request.facebook.graph.get_object('me')
    access_token = request.facebook.graph.access_token
    quote = random.choice(QUOTES)
    return render(request, 'home.html', {'me': me, 'access_token': access_token, 'quote': quote})

def update_status(request):
    quote = request.POST['quote']
    access_token = request.POST['access_token']
    graph = facebook.GraphAPI(access_token)
    graph.put_objects("me", "feed", message=quote)
    return render(request, 'all_done.html')