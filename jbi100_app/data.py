import datetime

import pandas as pd


def get_data():
    # Supress memory warning at startup
    return pd.read_csv("https://raw.githubusercontent.com/dbusn/JBI100-VIS/main/jbi100_app/datasets/dataset_clean.csv")


def get_coordinates():
    return pd.read_csv('https://raw.githubusercontent.com/dbusn/JBI100-VIS/main/jbi100_app/datasets/locations.csv')


def update_date(start_date, end_date):
    start_date_date = datetime.date.fromisoformat(start_date)
    end_date_date = datetime.date.fromisoformat(end_date)

    start_date_datetime = datetime.datetime.combine(start_date_date, datetime.datetime.min.time())
    end_date_datetime = datetime.datetime.combine(end_date_date, datetime.datetime.min.time())

    min_date = start_date_datetime.timestamp()
    max_date = end_date_datetime.timestamp()

    # Read data again
    df = get_data()

    date_list = df['Date'].tolist()
    i = 0
    for entry in date_list:
        row_date = entry.split("/")
        entry_date = datetime.datetime(int(row_date[2]), int(row_date[1]), int(row_date[0]), 0, 0, 0).timestamp()
        if entry_date < min_date or entry_date > max_date:
            df.drop(i, inplace=True)
        i += 1
    df = df.astype('str')

    return df
