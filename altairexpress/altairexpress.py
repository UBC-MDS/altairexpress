import pandas as pd
import altair as alt
import numpy as np


def hist(data, variable):
    """
    Creates a altair histogram indicating the position of the mean and median.

    Parameters
    ----------
    data : dataframe
        A pandas dataframe.
    variable : string
        A name of the variable inside data used to make the histogram.

    Returns
    --------
    altair plot
        Produces an altair histogram with vertical bars for the mean and median.

    Examples
    --------
    >>> from gapminder import gapminder
    >>> gapminder.head()
    >>> altairexpress.hist(gapminder, gdpPerCap)
    """
    # TODO raise an exception about the type of data. must be pandas dataframe

    # extract the variable
    v = data[variable]

    # TODO annotate plot with summary stats
    # get the variable statistics
    variable_mean = np.mean(v)
    variable_median = np.median(v)

    # set the x-axis position for annotations
    #annotation_x = np.max(v) * 0.9

    # TODO get the max frequency from scale of altair plot
    # get the max frequency
    # y_max = np.max(v)

    p1 = alt.Chart(data).mark_bar().encode(
        alt.X(variable),
        alt.Y('count()', stack=None))

    # Specify the axes
    mean_string = 'mean(' + variable + '):Q'
    median_string = 'median(' + variable + '):Q'


    mean_line = alt.Chart(data).mark_rule(color='red', size=5).encode(
        x=alt.X(mean_string))

    median_line = alt.Chart(data).mark_rule(color='blue', size=5).encode(
        x=alt.X(median_string))



    return p1 + mean_line + median_line


def ts_alt(data, col, type, frequency):
    """
    Convert csv file into a time series object, decompose it into in trend, seasonality/cyclicity
    and noise/remainder/error and plot the raw data and the decomposed components.

    Parameters
    ----------
    data : str
      the path of the csv file.
    type : str ("regular" or "irregular")
      "regular": time series with regular time intervals 
      "irregular": time series with irregular time intervals
    col : str
      the name of the column to be analyzed
    frequency: int
      the desired time interval



    Returns
    -------
    altair.vegalite.v3.api.Chart
      An altair figure with 4 subplots

    Examples
    --------
    >>> from altairexpress import altairexpress
    >>> altairexpress.ts_alt("https://raw.githubusercontent.com/plotly/datasets/master/timeseries.csv", A, irregular, 3)
    altair.vegalite.v3.api.Chart
    """

    print("hello")
