import plotly.express as px
import pandas as pd
import argparse
import datetime
from tqdm import tqdm

class plots:
    '''
    A class for processing results and plotting line graph using plotly.
    ...
    Attributes
    ----------
    input_file : str
        file containing daily frequencies.
    output_file : str
        name of static image file (jpeg) for saving the plot.
    title : str
        title of the plot.
    dates : list
        list of dates from the input file.
    counts : list
        count associated with each date from input file.

    Methods
    -------
    get_data():
        Reads data from input file and saves data in list form.
    plot():
        Plots and saves line graph for data using plotly.

    '''
    def __init__(self, input_file, output_file, title):
        self.input_file = input_file
        self.output_file = output_file
        self.title = title
        self.dates = []
        self.counts = []

    def get_data(self):
        '''
        Reads date,counts from input file and saves data in list form.
        Input  : Input file path
        Output : Two list of dates and counts associated with each date.
        '''
        file = open(self.input_file, 'r')
        lines = file.readlines()

        dates = []
        counts = []

        for line in tqdm(lines):
            date, count = line.split(",")
            count.strip()
            date.strip()
            dt = datetime.datetime.strptime(date, '%Y-%m-%d')
            dates.append(dt)
            counts.append(float(count))

        self.dates = dates
        self.counts = counts

    def plot(self):
        '''
        Plots and saves line graph for data using plotly.
        Input  : Two lists are used - Dates and count/values.
        Output : Plot is displayed in web browser and a static image is saved with output filename.
        '''
        df = pd.DataFrame(dict(
            x = self.dates,
            y = self.counts))
        fig = px.line(df, x="x", y="y", title=self.title) 
        fig.update_layout(
            xaxis_title="Date",
            yaxis_title=self.title)
        fig.show()
        fig.write_image(self.output_file+".jpeg")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Plot line graph and Save the graph")
    parser.add_argument("-input", help="Enter path of txt file with date, count",
                        dest="input_file", type=str, required=True)
    parser.add_argument("-output", help="Enter name of output file",
                        dest="output_filename", type=str, required=True)
    parser.add_argument("-title", help="Enter title fo the graph",
                        dest="title", type=str, required=True)

    args = parser.parse_args()

    input_file = args.input_file
    output_filename = args.output_filename
    title = args.title

    plts = plots(input_file, output_filename, title)
    plts.get_data()
    plts.plot()

