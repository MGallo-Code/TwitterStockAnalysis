from vader_sentiment.vader_sentiment import SentimentIntensityAnalyzer

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze(self, text):
        return self.analyzer.polarity_scores(text)