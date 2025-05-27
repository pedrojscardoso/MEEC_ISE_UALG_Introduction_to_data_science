import pandas as pd
import time
import panel as pn
from bokeh.plotting import figure
import psutil

delta = 0.1

# create a dataframe to store the data
df = pd.DataFrame(columns=['cpu', 'memory'])

def get_data():
    """ Get the CPU and memory usage, and store it in the dataframe. This is done using global df"""
    global df
    cpu = psutil.cpu_percent(delta)
    memory = psutil.virtual_memory().percent
    df.loc[pd.Timestamp.now()] = [cpu, memory]
    return df

def plot_line(df, column, plot, color='red'):
    """ Plot a line in the plot.
    :param df: dataframe
    :param column: column name (dataframe must have a column with this name)
    :param plot: bokeh plot
    :param color: color of the line
    """
    plot.line(x=df.index, y=df[column],
              line_width=2,
              legend_label=column,
              color=color,
              alpha=0.5)
    return plot


def make_feature_line_pane(feature, nrows=100):
    plot = plot_line(df=df[[feature]].dropna().tail(nrows),
                     column=feature,
                     plot=figure(x_axis_type="datetime"))
    return plot


def update_widgets():
    global df
    # update the dataframe
    get_data()

    # the log pane will show the last update time
    log_pane.object = f'Updated: {time.ctime()} '

    # the dataframe pane will show the last 10 rows of the dataframe
    df_pane.object = df.tail(10)

    # update the plots with the last 100 rows of the dataframe
    cpu_pane.object = make_feature_line_pane('cpu', nrows=100)
    memory_pane.object = make_feature_line_pane('memory', nrows=100)

    # update the gauges with the maximum value of the last 5 rows
    steps = 5
    cpu_gauge_pane.value = df['cpu'].iloc[-steps:].max()
    memory_gauge_pane.value = df['memory'].iloc[-steps:].max()

    # update the linear gauges with the maximum value of the last 5 rows
    cpu_linear_gauge_pane.value = df['cpu'].iloc[-steps:].max()
    memory_linear_gauge_pane.value = df['memory'].iloc[-steps:].max()

    # update the indicators with the maximum value of the last 5 rows
    cpu_indicator_pane.value = df['cpu'].iloc[-steps:].max()
    memory_indicator_pane.value = df['memory'].iloc[-steps:].max()



# ----------------------------
# Main
# ----------------------------
pn.extension('echarts')

# get the initial data
df = get_data()

# create the log pane, which will show the last update time (this is a markdown pane)
log_pane = pn.pane.Markdown('???', width=200, height=100)

# create a periodic callback to update the widgets - this will be called every delta seconds
callback = pn.state.add_periodic_callback(update_widgets, period=int(delta*1000))

# create the panes
# lineplot panes with the last 100 rows
cpu_pane = pn.pane.Bokeh(make_feature_line_pane('cpu'), width=600, height=300)
memory_pane = pn.pane.Bokeh(make_feature_line_pane('memory'), width=600, height=300)

# gauges with the maximum value of the last "step" rows
cpu_gauge_pane = pn.indicators.Gauge(name='CPU %', value=10, bounds=(0, 100), width=300, height=300)
memory_gauge_pane = pn.indicators.Gauge(name='Memory %', value=10, bounds=(0, 100), width=300, height=300)

# linear gauges with the maximum value of the last "step" rows
cpu_linear_gauge_pane = pn.indicators.LinearGauge(name='CPU %', value=10, bounds=(0, 100), width=150, height=300,
                                                  colors=[(33, 'green'), (66, 'gold'), (100, 'red')], horizontal=True)
memory_linear_gauge_pane = pn.indicators.LinearGauge(name='Memory %', value=10, bounds=(0, 100), width=150, height=300,
                                                     colors=[(33, 'green'), (66, 'gold'), (100, 'red')], horizontal=True)

# indicators with the maximum value of the last "step" rows
cpu_indicator_pane = pn.indicators.Number(name='CPU %', value=10, format='{value}%',
                                          colors=[(33, 'green'), (66, 'gold'), (100, 'red')])
memory_indicator_pane = pn.indicators.Number(name='Memory %', value=10, format='{value}%',
                                             colors=[(33, 'green'), (66, 'gold'), (100, 'red')])

# dataframe pane with the last "x" rows
df_pane = pn.pane.DataFrame(df)

#
layout = pn.layout.Column(
    pn.layout.Row("CPU",
        cpu_pane,
        cpu_gauge_pane,
        cpu_linear_gauge_pane,
        cpu_indicator_pane
    ),
    pn.layout.Row("Memory",
        memory_pane,
        memory_gauge_pane,
        memory_linear_gauge_pane,
        memory_indicator_pane
    ),
    pn.layout.Row(
        df_pane,
        log_pane
    )
).servable()
