import pandas as pd
import altair as alt


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