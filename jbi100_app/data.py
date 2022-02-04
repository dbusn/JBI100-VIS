import pandas as pd


# Read the default cleaned dataset for the barplot
def get_data():
    return pd.read_csv("https://raw.githubusercontent.com/dbusn/JBI100-VIS/main/jbi100_app/datasets/dataset_clean.csv")


# Read the coordinate data for the city selector
def get_coordinates():
    return pd.read_csv('https://raw.githubusercontent.com/dbusn/JBI100-VIS/main/jbi100_app/datasets/locations.csv')
