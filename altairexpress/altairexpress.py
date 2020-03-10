import pandas as pd
import altair as alt
# import numpy as np

import statsmodels.tsa.seasonal as sea


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
        Produces an altair histogram with
        vertical bars for the mean and median.

    Examples
    --------
    >>> from gapminder import gapminder
    >>> gapminder.head()
    >>> altairexpress.hist(gapminder, gdpPerCap)
    """
    # TODO raise an exception about the type of data. must be pandas dataframe

    # Check if data is dataframe
    assert isinstance(
        data, pd.DataFrame), "TypeError: Data must be a pandas dataframe."

    # Check if variable name is a string
    assert isinstance(variable, str), "Variable must be supplied as a string"

    # Check that variable is continuous numeric data
    assert pd.api.types.is_numeric_dtype(
        data[[variable]]), "Variable needs to be numeric. Your data must be \
            have a continuous numeric data type."

    # extract the variable
    # v = data[variable]

    # TODO annotate plot with summary stats
    # get the variable statistics
    # variable_mean = np.mean(v)
    # variable_median = np.median(v)

    # set the x-axis position for annotations
    # annotation_x = np.max(v) * 0.9

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


def ts_alt(data, col, frequency):
    """
    Convert csv file into a time series object, decompose it into in trend,
    seasonality/cyclicity and noise/remainder/error and plot the raw data and
    the decomposedcomponents. If the time series can't be decomposed, the
    function will just return the line chart of the raw data.

    Parameters
    ----------
    data : str
      the path of the csv file.
    col : str
      the name of the column to be analyzed
    frequency: {1, 4, 12, 52}
      the freqency of the time series



    Returns
    -------
    altair.vegalite.v3.api.Chart
      An altair figure with 4 subplots

    Examples
    --------
    >>> from altairexpress import altairexpress
    >>> altairexpress.ts_alt("https://raw.githubusercontent.com/plotly/, \
        datasets/master/timeseries.csv", A, 3)
    altair.vegalite.v3.api.Chart
    """
    # Check the variable type of inputs
    assert isinstance(
        data,
        str), "TypeError: The path of the data must be entered as a string."
    assert isinstance(
        col,
        str), "TypeError: The column name must be entered as a string."
    if (frequency not in [1, 4, 12, 52]):
        raise Exception(
            "ValueError: Frequency must be an integer from {1, 4, 12, 52}.")

    # load the data
    df_res = pd.read_csv(data, index_col=0, parse_dates=True).reset_index()

    # Check the input further
    if col not in df_res.columns:
        raise Exception(
            "ValueError: The column name were not found in the original data.")

    # Plot the raw data and decomposed components
    if frequency == 1:
        plt = alt.Chart(df_res).mark_line().encode(
            alt.X(df_res.columns[0]),
            alt.Y(col)
        ).properties(height=200, width=400)
    else:
        result = sea.seasonal_decompose(
            df_res[col], model='additive', period=frequency)
        res = result.resid.reset_index()
        trend = result.trend.reset_index()
        season = result.seasonal.reset_index()
        result_sum = pd.merge(
            pd.merge(pd.merge(res, trend), season), df_res.reset_index())
        res_df = pd.melt(result_sum, id_vars=[result_sum.columns[0]])
        if frequency == 4:
            x = str(df_res.columns[0]) + ":" + "O"
        else:
            x = str(df_res.columns[0]) + ":" + "T"
        plt = alt.Chart(res_df).mark_line().encode(
            alt.X(x),
            alt.Y("value:Q"),
            row=alt.Row('variable:N', sort=[col, 'seasonal', 'trend', 'resid'])
        ).properties(height=50, width=400)
    return plt
