from nltk.tokenize import word_tokenize 
from langdetect import detect
import nltk
from tqdm import tqdm
import demoji
import re
nltk.download('vader_lexicon')

class preprocessor:
    '''
    A class containing preprocessing techniques used for the messages.
    ...
    Attributes
    ----------
    messages : list
        all the messages in format (date,message text).

    Methods
    -------
    filter_non_english_messages():
        Discards non-English messages.
    specific_word_filter():
        Identifies messages with special words.
    '''

    def __init__(self, messages):
        self.messages = messages

    def filter_non_english_messages(self):
        '''
        Discards non-English messages.
        Input  : All messages.
        Output : List of messages [(date, message)]
        '''
        english_messages = []
        print("Filtering Non English messages......")
        for obj in tqdm(self.messages):
            d = obj[0]
            m = obj[1]

            # remove digits
            test = ''.join([i for i in m if (i.isalpha() or i==' ')])
            # remove trailing and leading whitespaces
            test = test.strip()

            if (len(test)==0):
                continue

            try:
                lang = detect(test)
            except:
                print(test)

            # The sentence with either all emojis or detected to be English will be used further 
            # else discarded
            if (len(demoji.findall_list(m)) == len(m) 
                or lang=='en'):
                english_messages.append((d,m))

        return english_messages

    def specific_word_filter(self,english_messages,specific_words):
        '''
        Identifies messages with special words.
        Input  : English messages.
        Output : List of messages containing special words [(date, message)] 
        '''
        specific_words = set([ w.lower() for w in list(specific_words) ])
        filtered_messages = []
        print("Detecting messages with specific words......")
        for obj in tqdm(english_messages):
            d = obj[0]
            m = obj[1]
            tokens = word_tokenize(m)
            if ( any([(w.lower() in specific_words) for w in tokens]) ):
                filtered_messages.append((d,' '.join(tokens)))
        return filtered_messages