from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('gettweet/<str:query>',views.get_tweets)
]
