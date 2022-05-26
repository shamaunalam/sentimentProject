from django.shortcuts import render
from . import analyze
# Create your views here.

def index(request):

    if request.method == 'POST':

        query = request.POST['query']

        return render(request,'index.html',analyze.get_sentiment(query))
    
    else:

        return render(request,'index.html')