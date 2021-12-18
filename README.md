# MINDS + Center on Knowledge Graphs  Programming Assignment

### Documentation for Code

[main](main.py) 

- Accepts arguments from the user. 
- Reads input data from input file, processes the messages and saves the output to the user-specified output file.
- Generates plots for messages per day and average sentiment per day.

[preprocessing](preprocessing.py)

- Utility for main.
- Discards non-english messages.
- Identifies messages with specific words.

[sentiment analyzer](sentiment_analyzer.py)

- Performs sentiment analysis on processed messages using Vader Sentiment analyis model.

[plot](plot.py)

- Accepts input text file, output filename and title for the graph, plots line graph using using plotly, displays and saves the static graph using the output filename.

***

### Instructions for running the script

- Clone the repository.

```
git clone https://github.com/priya-mane/MINDS-Center-on-Knowledge-Graphs_Programming_Assignment.git
```

- Create a Virtual Environment.

```
python -m venv env
```

- Activate the Virtual Enviornment we just created.

```
.\env\Scripts\activate
```

- Install dependencies.

```
pip install -r requirements.txt
```

- Run the script.

```
python main.py -i <input file path>.json -o <output filename>
```

Eg. 
```
python main.py -i telegram_messages.json -o output
```

- Plot Graphs

Mention input filename, output filename and the title for the graph

```
python plot.py -i <input file path>.txt -o <output filename for image> -t "<title for plot>"
```

Eg.

```
python plot.py -i daily_message_count.txt -o daily_message_count_plot -t "daily message count"
```

```
python plot.py -i avg_daily_sentiment.txt -o avg_daily_sentiment_plot -t "average daily sentiment"
```

- For knowing more about the scripts.

```
python main.py --help
```

```
python plot.py --help
```

- For details on class and their methods, import the class in python and use the following -

```
print(<class>.__doc__)
```

Eg.

```
print(preprocessor.__doc__) 
```

output - 

```
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
```


- For any uodates made, update the requirements.txt using.

```
pip freeze > requirements.txt
```
***


### Summary of Results

[Telegram messages](telegram_messages.json)
- Contains messages from telegram group Crypto.com from May 1, 2021 to May 15, 2021 in json format.

***

![Number of messages per day](daily_message_count_plot.jpeg)

***

![Average Sentiment per day](avg_daily_sentiment_plot.jpeg)


***


