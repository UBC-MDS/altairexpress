import pandas as pd
import numpy as np
import altair as alt


def fourier_transform(data, time_col, data_col):
    '''
    Creates Fourier transform plot of the data specified in the 'data_col' column. The frequency values are
    calculated from values on the 'time_col' column.

    Parameters
    ----------
    data: pandas.DataFrame
        pandas dataframe containing all neccessary information.
    time_col: str
        string containing the time data column corresponding to the data we
        want to apply fourier transform to.
    data_col: str
        string containing the name of the column we want to apply fourier transform to.


    Returns
    -------
    altair plot
        altair plot of frequency vs amplitude of the data inputed.


    Examples
    --------
    >>> my_data = pd.DataFrame(data = {'time_series': [0, 1, 2, 3],
                                       'signal': [2, 3, 4, 6]})
    >>> altairexpress.fourier_transform(data = my_data,
                                        time_col = 'time_series',
                                        data_col = 'signal')
    '''
    # Initial assertions that function arguments are correct
    assert isinstance(time_col, str), 'Column name for time data should be a string!'
    assert isinstance(data_col, str), 'Column name for signal data should be a string!'
    assert isinstance(data, pd.DataFrame), 'Data should be in pandas.DataFrame format!'

    # Loading data
    my_signal = np.array(data[data_col].dropna())
    my_time = np.array(data[time_col].dropna())

    # Making sure that there are no `NaN` values
    assert((data[data_col] == data[data_col].dropna()).all()), \
    '`NaN` values found in signal column!'
    assert((data[time_col] == data[time_col].dropna()).all()), \
    '`NaN` values found in time column!'

    sampling_freq = my_time[1] - my_time[0]
    for n in range(len(my_time) - 1):
        assert np.isclose(my_time[n + 1] - my_time[n], sampling_freq), \
        'Sampling time is not uniformly distributed! Assure that time between samples is constant!'

    amplitudes = np.fft.rfft(my_signal)
    frequencies = np.fft.rfftfreq(len(my_signal), sampling_freq)

    my_df = pd.DataFrame(data = {'Frequency': frequencies, 'Amplitude': amplitudes.real})

    my_plot = alt.Chart(my_df).mark_line().encode(
                x='Frequency',
                y='Amplitude')

    return my_plot
