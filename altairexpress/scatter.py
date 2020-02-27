def make_scatter(df, xval = None, yval = None, x_transform = False, y_transform = True):
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
    return