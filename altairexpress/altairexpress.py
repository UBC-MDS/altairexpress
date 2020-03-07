import pandas as pd
import altair as alt
import statsmodels.tsa.seasonal as sea

def hist(data, variable):
    """
    Creates a altair histogram indicating the position of the mean and median and displays the standard deviation.

    Parameters
    ----------
    data : dataframe
        A pandas dataframe.
    variable : string
        A name of the variable inside data used to make the histogram.

    Returns
    --------
    altair plot
        Produces an altair histogram with vertical bars for the mean and median and annotates the standard deviation.

    Examples
    --------
    >>> from gapminder import gapminder
    >>> gapminder.head()
    >>> altairexpress.hist(gapminder, gdpPerCap)
    """
    print("hello MDS")


def ts_alt(data, col, frequency):
    """
    Convert csv file into a time series object, decompose it into in trend, seasonality/cyclicity
    and noise/remainder/error and plot the raw data and the decomposed components.

    Parameters
    ----------
    data : str
      the path of the csv file.
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
    >>> altairexpress.ts_alt("https://raw.githubusercontent.com/plotly/datasets/master/timeseries.csv", A, 3)
    altair.vegalite.v3.api.Chart
    """
    
    df = pd.read_csv(data, index_col=0, parse_dates=True)
    df_res = df.reset_index()

    if frequency == 1:
        plt =  alt.Chart(df_res).mark_line().encode(
            alt.X(df_res.columns[0]),
            alt.Y(col)
          ).properties(height=200, width=400)
    else:
        result = sea.seasonal_decompose(df[col], model='additive', period=frequency)
        res = result.resid.reset_index()
        trend = result.trend.reset_index()
        season = result.seasonal.reset_index()
        result_sum = pd.merge(pd.merge(pd.merge(res, trend), season), df.reset_index())
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