import pandas as pd
import altair as alt
import numpy as np
import statsmodels.tsa.seasonal as sea


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
    frequency: int
      the freqency of the time series, should choose from {1, 4, 12, 52}



    Returns
    -------
    altair.vegalite.v3.api.Chart
      An altair figure with 4 subplots

    Examples
    --------
    >>> from altairexpress import ts
    >>> ts_alt("extdata\example_data.csv", "earnings", 4)
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
