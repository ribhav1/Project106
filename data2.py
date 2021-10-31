import numpy as np
import plotly_express as px
import csv

def plot_figure(data_path):
    with open('Student Marks vs Days Present.csv') as f:
        file_data = csv.DictReader(f)
        scatter_plot = px.scatter(file_data, x='Marks In Percentage', y='Days Present')
        scatter_plot.show()

def get_data_source(data_path):
    coffe = []
    hours_of_sleep = []
    with open('Student Marks vs Days Present.csv') as f:
        file_data = csv.DictReader(f)
        for row in file_data:
            coffe.append(float(row["Marks In Percentage"]))
            hours_of_sleep.append(float(row["Days Present"]))
    return {"x": coffe, "y": hours_of_sleep}

def find_correlation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("correlation between Marks In Percentage vs Days Present: " + str(correlation[0,1]))

def setup():
    data_path = "Student Marks vs Days Present.csv"
    data_source = get_data_source(data_path)
    find_correlation(data_source)
    plot_figure(data_path)

setup()