import pandas as pd
# import pandas_bokeh
import seaborn as sns
import time
import panel as pn
from bokeh.plotting import figure, show

import yfinance as yf
def get_data(ticker, n_days=1, interval=1):
    ticker = yf.Ticker(ticker)
    # see https://algotrading101.com/learn/yfinance-guide/ for more examples
    df = ticker.history(period=f'{n_days}D', interval=f'{interval}m')
    return df

def resample_data(df, interval):
    df_resampled = df\
        .resample(interval)\
        .agg({'Open': 'first', 'High': 'max', 'Low': 'min', 'Close': 'last'})
    return df_resampled


def plot_line(df, column, color, plot):
    plot.line(x=df.index,
              y=df[column],
              line_width=2,
              legend_label=column,
              color=color,
              alpha=0.5)
    return plot


def plot_multiple_lines(df, columns, plot):
    # plot = figure(x_axis_type="datetime")
    colors = ['blue', 'green', 'red', 'orange']
    for column, color in zip(columns, colors):
        plot_line(df, column, color, plot)

    return plot


def update_widgets(event):

    stock = stocks_panel.value
    df = get_data(stock, n_days=1, interval=15)
    df = resample_data(df, '15min')

    columns = columns_panel.value

    log_pane.object = f'{time.ctime()}: Loaded data for {stock} with columns {columns}'

    plot = plot_multiple_lines(df=df,
                               columns=columns,
                               plot=figure(x_axis_type="datetime"))
    stock_evolution_panel.object = plot




def make_stocks_select_panel():
    stocks_panel = pn.widgets.Select(
        options=['BTC-USD', 'ETH-USD', 'LTC-USD'],
        value=['BTC-USD'],
        # size=6,
        name='Cryptocurrencies'
    )
    pn.bind(update_widgets, stocks_panel, watch=True)
    return stocks_panel


def make_columns_select_panel():
    columns_panel = pn.widgets.MultiChoice(
        options=['Open', 'Close', 'High', 'Low'],
        value=['Open', 'Close'],
        name='Columns'
    )
    pn.bind(update_widgets, columns_panel, watch=True)
    return columns_panel

def make_stocks_evolution_panel():
    return pn.pane.Bokeh(
        plot_multiple_lines(df=df_resampled,
                            columns=['Open', 'Close'],
                            plot=figure(x_axis_type="datetime")),
        width=800,
        height=400
    )

def make_switch_panel():
    switch = pn.widgets.Switch(name='Start/Stop', value=False)
    pn.bind(update_widgets, switch, watch=True)
    return switch


# ----------------------------
# Main
# ----------------------------
pn.extension()

df = get_data('BTC-USD', n_days=7, interval=1)
df_resampled = resample_data(df, '30min')

stocks_panel = make_stocks_select_panel()
columns_panel = make_columns_select_panel()
stock_evolution_panel = make_stocks_evolution_panel()


filter_panel = pn.layout.Column(
    stocks_panel,
    columns_panel,
)


# update_widgets will be called every time the value of stocks_panel or columns_panel changes
def refresh():
    update_widgets(None)
callback = pn.state.add_periodic_callback(refresh, period=1000)

log_pane = pn.pane.Markdown('??? info')

layout = pn.layout.Column(
    filter_panel,
    stock_evolution_panel,
    log_pane,
    #callback
).servable()