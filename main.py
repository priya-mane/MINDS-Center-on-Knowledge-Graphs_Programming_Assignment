from sentiment_analyzer import sentiment_analyzer
from preprocessing import preprocessor
from tqdm import tqdm
import argparse
import json
from datetime import datetime
from collections import Counter

class messages_processor:
    def __init__(self,input_file, output_file, specific_words):
        self.messages = []
        self.english_messages = []
        self.specific_messages = []
        self.sentiments = []
        self.specific_words = specific_words
        self.input_file = input_file
        self.output_file = output_file

    def read_input(self):
        data = json.load(open(self.input_file,"r", encoding='utf8'))
        print("Reading messages......")

        for m in tqdm(data["messages"]):
            dt = datetime.strptime(m['date'], "%Y-%m-%dT%H:%M:%S")
            msg_txt = m['text']

            if (type(msg_txt)==str):
                text = msg_txt
            else:
                text = ""
                for t in msg_txt:
                    if (type(t)==str):
                        text += t

            self.messages.append((dt.strftime("%Y-%m-%d"), text))
            
    def process(self):
        prep = preprocessor(self.messages)
        self.english_messages = prep.filter_non_english_messages()
        self.specific_messages = prep.specific_word_filter(self.english_messages, self.specific_words)

        sentiment_a = sentiment_analyzer(self.specific_messages) 
        self.sentiments = sentiment_a.sentiment_analysis()
        self.save_result()

    def get_avg_sentiment_and_day_count(self):
        daily_sentiment_tracker = Counter()
        day_counter = Counter()

        for d,_,pol in self.sentiments:
            daily_sentiment_tracker[d] += pol
            day_counter[d] += 1

        for d in daily_sentiment_tracker.keys():
            daily_sentiment_tracker[d] = float(daily_sentiment_tracker[d]/day_counter[d])

        f = open("daily_message_count.txt", "w")
        for day, count in day_counter.items():
            f.write("%s, %d" % (day, count) + "\n")
        f.close()

        f = open("avg_daily_sentiment.txt", "w")
        for day, avg_sentiment in daily_sentiment_tracker.items():
            f.write("%s, %f" % (day, avg_sentiment) + "\n")
        f.close()

    def save_result(self):
        result = {}
        print("Saving output......")
        for i in tqdm(range(len(self.specific_messages))):
            d,m = self.specific_messages[i]
            d,s,_ = self.sentiments[i]
            result[i] = {
                "date": d,
                "message":m,
                "sentiment":s
            }

        with open(self.output_file +'.json', 'w') as f:
            json.dump(result, f, indent=2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Preprocess telegram messages and perform sentiment analysis for the same")
    parser.add_argument("-input", help="Enter path of json file with telegram messages",
                        dest="input_file", type=str, required=True)
    parser.add_argument("-output", help="Enter name of output file",
                        dest="output_filename", type=str, required=True)

    args = parser.parse_args()

    input_file = args.input_file
    output_filename = args.output_filename

    msg_pro = messages_processor(input_file, output_filename, set(['SHIB', 'DOGE']))
    msg_pro.read_input()
    msg_pro.process()
    msg_pro.get_avg_sentiment_and_day_count()


                









