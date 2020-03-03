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

   
    # Type Checks
    assert isinstance(df, pd.DataFrame), "TypeError: Data must be entered as a pandas dataframe."
    assert isinstance(xval, str), "Wrong type! X-axis variable must be entered and be of type String."
    assert isinstance(yval, str), "Wrong type! X-axis variable must be entered and be of type String."
    assert isinstance(x_transform, bool), "TypeError: x_transform must be of type boolean."
    assert isinstance(y_transform, bool), "TypeError: y_transform must be of type boolean."
    
    if xval not in df.columns:
        raise Exception("Variable name not found in input dataframe. Double-check spelling!")
    
    assert pd.api.types.is_numeric_dtype(df[xval]), "Your x-variable needs to be numeric. Double-check dtype and coerce to numeric if necessary."
    assert pd.api.types.is_numeric_dtype(df[yval]), "Your y-variable needs to be numeric. Double-check dtype and coerce to numeric if necessary."  
    



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