import nltk
from textblob import TextBlob


def get_sentiment(query):

    data = TextBlob(query)

    s = data.sentiment

    if s[1]<=0.5:
        sub = "Fact"
    elif s[1]>0.5:
        sub = "Opinion"

    return {"polarity":(s[0]+1)/2,"subjectivity":sub}