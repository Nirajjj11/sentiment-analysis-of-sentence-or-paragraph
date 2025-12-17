from django.shortcuts import render
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

def sentiment_home(request):
    content = request.GET.get('sentence', '')
    result = ''
    score = {}

    if content:
        sia = SentimentIntensityAnalyzer()
        score = sia.polarity_scores(content)

        if score['compound'] >= 0.5:
            result = "Sentence is Positive 🙂"
        elif score['compound'] <= -0.5:
            result = "Sentence is Negative 🙁"
        else:
            result = "Sentence is Neutral 😐"

    data = {
        'score': score,
        'result': result,
        'sentence': content
    }

    return render(request, 'sentiment.html', data)
