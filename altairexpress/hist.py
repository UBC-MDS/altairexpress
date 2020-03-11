import altair as alt
import numpy as np
import pandas as pd


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
        Produces an altair histogram with vertical
        bars for the mean and median.

    Examples
    --------
    >>> from gapminder import gapminder
    >>> gapminder.head()
    >>> altairexpress.hist(gapminder, gdpPerCap)
    """

    # Check if data is dataframe
    assert isinstance(data, pd.DataFrame), "TypeError: Data must be a pandas "\
                                           "dataframe. "

    # Check if variable name is a string
    assert isinstance(variable, str), "TypeError: Variable must be supplied " \
                                      "as a string "

    # # Check that variable is continuous numeric data
    # assert pd.api.types.is_numeric_dtype(
    #     data[variable]), "Variable needs to be numeric. Your data must be " \
    #                      "have a continuous numeric data type. "

    # check that variable is contained in data
    # assert variable in data.columns, "NameError: Variable provided is not " \
    #                                  "contained in data "

    # extract the variable
    v = data[variable]

    # get the variable statistics
    mean = np.round(np.mean(v), 2)
    median = np.round(np.median(v), 2)
    std_dev = np.round(np.std(v), 2)

    # set the x-axis position for annotations
    annotation_x = np.max(v) * 0.9

    # make base histogram
    p1 = alt.Chart(data).mark_bar().encode(
        alt.X(variable, bin=True, title=variable),
        alt.Y('count()', title="Count")
    ).properties(title="Distribution of {0}".format(variable))

    # Specify summary statistic annotations
    annot1 = (
        alt.Chart(data).mark_text(
            color='pink',
            text="Mean is {0:.2f}".format(mean)).encode(
            alt.X('xval:Q'),
            alt.Y('yval:Q')).transform_calculate(
            xval=str(annotation_x),
            yval=str(np.mean(np.arange(0, 500))))
    )

    annot2 = (
        alt.Chart(data).mark_text(
            color='red',
            text="Median is {0:.2f}".format(median)).encode(
            alt.X("xval:Q"),
            alt.Y("yval:Q")).transform_calculate(
            xval=str(annotation_x),
            yval=str(np.mean(np.arange(0, 450))))
    )

    annot3 = (
        alt.Chart(data).mark_text(
            color='blue',
            text="Standard Dev is {0:.2f}".format(std_dev)).encode(
            alt.X("xval:Q"),
            alt.Y("yval:Q")).transform_calculate(
            xval=str(annotation_x),
            yval=str(np.mean(np.arange(0, 400))))
    )

    # make vertical bars for mean and median
    mean_string = 'mean(' + variable + '):Q'
    median_string = 'median(' + variable + '):Q'

    mean_line = (
        alt.Chart(data).mark_rule(color='pink',
                                  size=5).encode(alt.X(mean_string,
                                                       title=variable))
    )

    median_line = (
        alt.Chart(data).mark_rule(color='red',
                                  size=5).encode(alt.X(median_string,
                                                       title=variable))
    )

    return p1 + annot1 + annot2 + annot3 + mean_line + median_line
