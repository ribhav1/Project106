import numpy as np
import plotly_express as px
import csv

def plot_figure(data_path):
    with open('cups of coffee vs hours of sleep.csv') as f:
        file_data = csv.DictReader(f)
        scatter_plot = px.scatter(file_data, x='Coffee in ml', y='sleep in hours')
        scatter_plot.show()

def get_data_source(data_path):
    coffe = []
    hours_of_sleep = []
    with open('cups of coffee vs hours of sleep.csv') as f:
        file_data = csv.DictReader(f)
        for row in file_data:
            coffe.append(float(row["Coffee in ml"]))
            hours_of_sleep.append(float(row["sleep in hours"]))
    return {"x": coffe, "y": hours_of_sleep}

def find_correlation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("correlation between Coffee in ml vs sleep in hours: " + str(correlation[0,1]))

def setup():
    data_path = "cups of coffee vs hours of sleep.csv"
    data_source = get_data_source(data_path)
    find_correlation(data_source)
    plot_figure(data_path)

setup()