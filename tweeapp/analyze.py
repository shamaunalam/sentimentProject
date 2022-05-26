import nltk
from textblob import TextBlob


def get_sentiment(query):

    data = TextBlob(query)

    s = data.sentiment


    return {"polarity":(s[0]+1)/2,"subjectivity":s[1]}