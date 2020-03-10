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

    # Check if data is dataframe
    assert isinstance(data, pd.DataFrame), "TypeError: Data must be a pandas dataframe."

    # Check if variable name is a string
    assert isinstance(variable, str), "Variable must be supplied as a string"

    # Check that variable is continuous numeric data
    assert pd.api.types.is_numeric_dtype(
        data[[variable]]), "Variable needs to be numeric. Your data must be have a continuous numeric data type."

    # extract the variable
    v = data[variable]

    # TODO annotate plot with summary stats
    # get the variable statistics
    variable_mean = np.mean(v)
    variable_median = np.median(v)
    variable_sd = np.std(v)

    # set the x-axis position for annotations
    annotation_x = np.max(v) * 0.9

    # TODO get the max frequency from scale of altair plot
    # get the max frequency
    # y_max = np.max(v)

    # make base histogram 
    p1 = alt.Chart(data).mark_bar().encode(
        alt.X(variable, bin=True, title=variable),
        alt.Y('count()', title="Count").properties(title="Distribution of {0}".format(variable))

    # Specify annotations 
    annotation = (alt.Chart(data)
    .mark_text(color = 'pink',
    text="Mean is {0:.2f}".format(variable_mean))
    .transform_calculate(x_val = str(annotation_x),
    y_val = str(np.mean(np.arange(0, 600))))


    annotation2 = (alt.Chart(data)
                   .mark_text(color = 'red', text="Median is {0:.2f}".format(variable_median))
                   .encode(alt.X("x_val:Q"), alt.Y("y_val:Q"))
                   .transform_calculate(x_val = str(annotation_x),
                                        y_val = str(np.median(np.arange(0, 500)))))

    annotation3 = (alt.Chart(data)
                   .mark_text(color = 'blue', text="Standard Dev is {0:.2f}".format(variable_sd))
                   .encode(alt.X("x_val:Q"), alt.Y("y_val:Q"))
                   .transform_calculate(x_val = str(annotation_x),
                                        y_val = str(np.std(np.arange(0, 400)))))




    # Specify the axes
    mean_string = 'mean(' + variable + '):Q'
    median_string = 'median(' + variable + '):Q'


    mean_line = alt.Chart(data).mark_rule(color='red', size=5).encode(
        x=alt.X(mean_string))

    median_line = alt.Chart(data).mark_rule(color='blue', size=5).encode(
        x=alt.X(median_string))



    return p1 + mean_line + median_line + annotation + annotation2, annotation3