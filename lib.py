"""file for modules"""

import pandas as pd


def load_data(dataset):
    "load data from csv into pandas dataframe"
    data = pd.read_csv(dataset)
    return data
