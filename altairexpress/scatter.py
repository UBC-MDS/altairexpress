import altair as alt
import numpy as np


def make_scatter(df, xval = None, yval = None, x_transform = False, y_transform = False):
    '''
    Takes in a dataframe and creates a scatterplot that compares two numerical features/variables that are specified by the user.
    Additionally, the user can toggle natural log transformations on both the x and y axis.

    Arguements:

    df - (dataframe) Dataframe 
    xval - (String) variable/column name 
    yval - (String) variable/column name
    x_logtransform - (Boolean) determines whether a natural log transformation occurs on the x-axis
    y_logtransform - (Boolean) determines whether a natural log transformation occurs on the y-axis
    '''



    if x_transform == "log":
        df[xval] = np.log(df[xval])

    if y_transform == "log":
        df[yval] = np.log(df[yval])
    
    x_scale = alt.Scale(domain = (float(df[xval].min()), float(df[xval].max())))
    y_scale = alt.Scale(domain = (float(df[yval].min()), float(df[yval].max())))

    scatter = alt.Chart(df).mark_circle(size=90, opacity = 0.3).encode(
                alt.X(xval, scale = x_scale),
                alt.Y(yval, scale = y_scale)
            ).properties(width=300, height=200)

    x_hist = alt.Chart(df).mark_bar(opacity = 0.3).encode(
            alt.X(xval, bin=alt.Bin(extent = x_scale.domain), title = ""),
            alt.Y('count()', stack = None)               
        ).properties(title='{0} distribution'.format(xval),
                        width=300, height=100)

    y_hist = alt.Chart(df).mark_bar(opacity = 0.4).encode(
        alt.X('count()', stack = None),
        alt.Y(yval, bin = alt.Bin(extent = y_scale.domain), title = "")
        ).properties(title='{0} distribution'.format(yval),
                        width=100, height=200)

    return (x_hist & (scatter | y_hist)).configure_view(strokeWidth=0)