#!/usr/bin/env python3

from chart import Chart
import pandas as pd

data = pd.read_csv(
    f"ticker_data/ETHUSD-1d-data.csv",
    parse_dates=[0],
    usecols=['timestamp', 'close', 'open', 'high', 'low', 'volume']
)
chart = Chart(data)
actions = [
    ("2020-01-01", "BUY"),
    ("2020-02-01", "BUY"),
    ("2020-03-01", "BUY"),
    ("2020-04-01", "BUY"),
    ("2020-05-01", "BUY"),
    ("2020-06-01", "BUY"),
    ("2020-07-01", "BUY"),
    ("2020-08-01", "BUY"),
    ("2020-09-01", "BUY"),
    ("2020-01-20", "SELL"),
    ("2020-02-20", "SELL"),
    ("2020-03-20", "SELL"),
    ("2020-04-20", "SELL"),
    ("2020-05-20", "SELL"),
    ("2020-06-20", "SELL"),
    ("2020-07-20", "SELL"),
    ("2020-08-20", "SELL"),
    ("2020-09-20", "SELL"),
]
chart.add_actions(actions)
chart.plot()
