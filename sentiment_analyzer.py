from nltk.sentiment.vader import SentimentIntensityAnalyzer
from tqdm import tqdm

class sentiment_analyzer:
    '''
    A class containing technique for sentiment analysis.
    ...
    Attributes
    ----------
    messages : list
        English messages filtered using the preprocessing module in format (date, message text).

    Methods
    -------
    sentiment_analysis():
        Performs sentiment analysis on messages using Vader sentiment analysis model.

    '''
    def __init__(self, messages):
        self.messages = messages

    def sentiment_analysis(self):
        '''
        Performs sentiment analysis on messages using Vader sentiment analysis model.
        Input  : Telegram messages
        Output : Classified sentences with compound polarity value.
        '''
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