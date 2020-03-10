import altair as alt
import numpy as np
import pandas as pd
import warnings


def make_scatter(data,
                 xval=None,
                 yval=None,
                 x_transform=False,
                 y_transform=False):
    """
    Takes in a dataframe and creates a scatterplot that compares two numerical
    features/variables that are specified by the user. Additionally, the user
    can toggle natural log transformations on both the x and y axis.

    Parameters
    ----------
    data : pandas.core.frame.DataFrame
       Input dataframe.
    xval : str
      Variable used to represent the x-axis.
    yval : str
      Variable used to represent the y-axis
    x_logtransform : bool
      Determines whether a log transformation occurs on the x-axis.
    y_logtransform : bool
      Determines whether a log transformation occurs on the x-axis.

    Returns
    -------
    altair.vegalite.v3.api.VConcatChart
      Scatterplot of user-specified variables, along with associated histograms.

    Examples
    --------
    >>> from altairexpress import scatter
    >>> from vega_datasets import data
    >>> make_scatter(data.cars(), xval = "Horsepower", yval = "Acceleration")
    """
    # create a copy of the dataframe so that original dataframe
    #  remains unchanged
    df = data.copy(deep=True)

    # Check to ensure variable types are appropriate
    error_one = "TypeError: Data must be entered as a pandas dataframe."
    assert isinstance(df, pd.DataFrame), error_one
    error_two = "Wrong type! X-axis variable must be entered as a String."
    assert isinstance(xval, str), error_two
    error_three = "Wrong type! X-axis variable must be entered as a String."
    assert isinstance(yval, str), error_three
    error_four = "TypeError: x_transform must be of type boolean."
    assert isinstance(x_transform, bool), error_four
    error_five = "TypeError: y_transform must be of type boolean."
    assert isinstance(y_transform, bool), error_five

    # Ensure variable exists in the dataframe
    if xval not in df.columns or yval not in df.columns:
        raise ValueError("Variable name not found in input dataframe.")

    # Ensure variable is numeric
    error_msg_x = "Your x-variable needs to be numeric."
    assert pd.api.types.is_numeric_dtype(df[xval]), error_msg_x

    error_msg_y = "Your y-variable needs to be numeric."
    assert pd.api.types.is_numeric_dtype(df[yval]), error_msg_y

    # Toggle a log transformation on the x-axis
    warn_one = "Can't have negative x values with np.log"
    if x_transform:
        if any(df[xval] < 0):
            warnings.warn(warn_one)
        df[xval] = np.log(df[xval])

    # Toggle a log transformation on the y-axis
    warn_two = "Can't have negative y values with np.log"
    if y_transform:
        if any(df[yval] < 0):
            warnings.warn(warn_two)
        df[yval] = np.log(df[yval])

    # Update scale bounds of the plots
    x_scale = alt.Scale(domain=(float(df[xval].min()), float(df[xval].max())))
    y_scale = alt.Scale(domain=(float(df[yval].min()), float(df[yval].max())))

    # Create base scatterplot
    scatter = alt.Chart(df).mark_circle(size=90, opacity=0.3).encode(
                alt.X(xval, scale=x_scale),
                alt.Y(yval, scale=y_scale)
            ).properties(width=300, height=200)

    # Create x-histogram
    x_hist = alt.Chart(df).mark_bar(opacity=0.3).encode(
            alt.X(xval, bin=alt.Bin(extent=x_scale.domain), title=""),
            alt.Y('count()', stack=None)
        ).properties(title='{0} distribution'.format(xval),
                     width=300, height=100)

    # Create y-histogram
    y_hist = alt.Chart(df).mark_bar(opacity=0.4).encode(
        alt.X('count()', stack=None),
        alt.Y(yval, bin=alt.Bin(extent=y_scale.domain), title="")
        ).properties(title='{0} distribution'.format(yval),
                     width=100, height=200)

    return (x_hist & (scatter | y_hist)).configure_view(strokeWidth=0)
