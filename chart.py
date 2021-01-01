#!/usr/bin/env python3

import plotly.graph_objects as plotly
import pandas as pd
from time import time

class Chart():
    def __init__(self, data,
            timestamp_col = 'timestamp',
            open_col = 'open',
            high_col = 'high',
            low_col = 'low',
            close_col = 'close'
            ):
        self.data = data
        self.timestamp_col = timestamp_col
        self.open_col = open_col
        self.high_col = high_col
        self.low_col = low_col
        self.close_col = close_col
        self.figure = self.create_figure()
        self.actions = []

    def create_figure(self):
        return plotly.Figure(data=[plotly.Candlestick(
            x=self.data[self.timestamp_col],
            open=self.data[self.open_col],
            high=self.data[self.high_col],
            low=self.data[self.low_col],
            close=self.data[self.close_col],
            )])

    def add_actions(self, actions):
        self.actions = actions

    def candle(self, date):
        return self.data.loc[self.data[self.timestamp_col] == date]

    def add_buys(self):
        buys = [i for i in self.actions if i[1] == 'BUY']
        self.figure.add_trace(plotly.Scatter(
            x=[i[0] for i in buys],
            y=[self.candle(i[0]).low.values[0] for i in buys],
            mode='markers',
            name='BUYS',
            marker_symbol='triangle-up',
            marker=dict(
                color='green',
                size=10,
                ),
            ))

    def add_sells(self):
        sells = [i for i in self.actions if i[1] == 'SELL']
        self.figure.add_trace(plotly.Scatter(
            x=[i[0] for i in sells],
            y=[self.candle(i[0]).high.values[0] for i in sells],
            mode='markers',
            name='SELLS',
            marker_symbol='triangle-down',
            marker=dict(
                color='red',
                size=10,
                ),
            ))

    def plot(self, image=False):
        self.add_sells()
        self.add_buys()
        self.figure.update_layout(xaxis_rangeslider_visible=False)
        if image:
            self.figure.write_image(f"images/{time()}.svg")
        else:
            self.figure.show()
