import pandas as pd
import altair as alt
import statsmodels.tsa.seasonal as sea


def ts_alt(data, col, frequency):
    """
    Convert a dataframe into a time series object, decompose it into in trend,
    seasonality/cyclicity and noise/remainder/error and plot the raw data and
    the decomposedcomponents. If the time series can't be decomposed, the
    function will just return the line chart of the raw data.

    Parameters
    ----------
    data : pandas.DataFrame
        pandas dataframe containing all neccessary information.
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
    >>> import pandas as pd
    >>> time = ["1950 Q1", "1950 Q2", "1950 Q3", "1950 Q4",
    >>> "1951 Q1", "1951 Q2", "1951 Q3", "1951 Q4"]
    >>> earnings = [0.71, 0.63, 0.82, 0.91,
    >>> 0.71, 0.63, 0.82, 0.91]
    >>> ts_data = pd.DataFrame({"time" : time, "earnings" : earnings})
    >>> ts_alt(ts_data, "earnings", 4)
    """
    # Check the variable type of inputs
    assert isinstance(
        data,
        pd.DataFrame), \
        "TypeError: The data must be in pandas.DataFrame format."
    assert isinstance(
        col,
        str), "TypeError: The column name must be entered as a string."
    if (frequency not in [1, 4, 12, 52]):
        raise Exception(
            "ValueError: Frequency must be an integer from {1, 4, 12, 52}.")

    # create a copy of the dataframe so that original dataframe
    #  remains unchanged
    df = data.copy(deep=True)

    # Check the input further
    if col not in df.columns:
        raise Exception(
            "ValueError: The column name were not found in the original data.")

    # Plot the raw data and decomposed components
    if frequency == 1:
        plt = alt.Chart(df).mark_line().encode(
            alt.X(df.columns[0]),
            alt.Y(col)
        ).properties(height=200, width=400)
    else:
        result = sea.seasonal_decompose(
            df[col], model='additive', period=frequency)
        res = result.resid
        trend = result.trend
        season = result.seasonal
        result_sum = pd.DataFrame({'date': df.iloc[:, 0],
                                'raw': df[col],
                                    'trend': trend,
                                    'season': season,
                                    'residual': res})
        res_df = pd.melt(result_sum, id_vars=[result_sum.columns[0]])
        if frequency == 4:
            x = str(res_df.columns[0]) + ":" + "O"
        else:
            x = str(res_df.columns[0]) + ":" + "T"
        plt = alt.Chart(res_df).mark_line().encode(
            alt.X(x),
            alt.Y("value:Q"),
            row=alt.Row('variable:N',
                        sort=['raw', 'trend', 'season', 'residual'])
        ).properties(height=50, width=400)
    return plt
