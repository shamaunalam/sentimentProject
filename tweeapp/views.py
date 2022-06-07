from django.shortcuts import render
from django.http import JsonResponse
from . import analyze
# Create your views here.

from .twitterapi import BEARER_TOKEN , search_twitter

def index(request):

    if request.method == 'POST':

        query = request.POST['query']
        return render(request,'index.html',analyze.get_sentiment(query))
    
    else:

        return render(request,'index.html')


def get_tweets(request,query):

    tweet_fields = "tweet.fields=text"
    
    #twitter api call
    json_response = search_twitter(query=query, tweet_fields=tweet_fields, bearer_token=BEARER_TOKEN)

    content = dict()
    for i,t in enumerate(json_response['data']):
        content.update({i:{'tweet':t['text'],'sent':analyze.get_sentiment(t['text'])}})

    
    return render(request,'tweet.html',{'content':content})
