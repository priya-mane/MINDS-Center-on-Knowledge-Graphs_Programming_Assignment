import plotly.express as px
import pandas as pd
import argparse
import datetime

class plots:
    def __init__(self, input_file, output_file, title):
        self.input_file = input_file
        self.output_file = output_file
        self.dates = []
        self.counts = []
        self.title = title

    def get_data(self):
        file = open(self.input_file, 'r')
        lines = file.readlines()

        dates = []
        counts = []

        for line in lines:
            date, count = line.split(",")
            count.strip()
            date.strip()
            dt = datetime.datetime.strptime(date, '%Y-%m-%d')
            dates.append(dt)
            counts.append(float(count))

        self.dates = dates
        self.counts = counts

    def plot(self):
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

