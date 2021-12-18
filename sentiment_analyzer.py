from nltk.sentiment.vader import SentimentIntensityAnalyzer
from tqdm import tqdm

class sentiment_analyzer:
    def __init__(self, messages):
        self.messages = messages

    def sentiment_analysis(self):
        sid = SentimentIntensityAnalyzer()
        sentiments = []
        print("Analysing message sentiment......")
        for obj in tqdm(self.messages):
            d = obj[0]
            m = obj[1]
            polarities = sid.polarity_scores(m)
            if polarities['compound'] >= 0.5:
                sentiment = 'positive'
            elif polarities['compound'] <= -0.5:
                sentiment = 'negative'
            else:
                sentiment = 'neutral'

            sentiments.append((d, sentiment, polarities['compound']))
            
        return sentiments