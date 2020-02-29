import pandas as pd
import numpy as np
import altair as alt


def fourier_transform(data, time_col, data_col):
    '''
    Creates fourier transform plot of the data specified in the 'time_col' column

    Parameters
    ----------
    data: dataframe
        pandas dataframe containing all neccessary information
    time_col: str
        string containing the time data column corresponding to the data we
        want to apply fourier transform to
    data_col: str
        string containing the name of the column we want to apply fourier transform to


    Returns
    -------
    altair plot
        altair plot of frequency vs amplitude of the data inputed


    Examples
    --------
    >>> my_data = pd.DataFrame(data = {'time_series': [0, 1, 2, 3],
                                       'signal': [2, 3, 4, 6]})
    >>> altairexpress.fourier_transform(data = my_data,
                                        time_col = 'time_series',
                                        data_col = 'signal')
    '''
    print('no compilation error!')
