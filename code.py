import pandas as pd
import statistics
import plotly.figure_factory as ff
import random
 
df = pd.read_csv("medium_data.csv")
data = df["reading_time"].to_list()

population_mean = statistics.mean(data)
print("population mean is {}".format(population_mean))

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    print("sample mean is {}".format(mean))
    return mean

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["reading time"], show_hist = False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0, 100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)

setup()