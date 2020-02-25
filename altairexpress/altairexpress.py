import altair as alt

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