from altairexpress import fourier_transform as ft
import pandas as pd
import numpy as np
import altair as alt


def test_fourier():
    """
    Tests the fourier function fourier_transform to make sure the outputs are
    correctly rendering.
    Returns:
    --------
    None
        The test should pass and no asserts should be displayed.
    """
    # Creating test DataFrame objects
    N = 600
    T = 1.0 / 800.0
    x = np.linspace(0.0, N*T, N)
    y1 = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
    y2 = np.sin(40.0 * 2.0*np.pi*x) + 0.5*np.sin(70.0 * 2.0*np.pi*x)
    my_df1 = pd.DataFrame(data={'X1': x, 'X2': y1})
    my_df2 = pd.DataFrame(data={'X1': x, 'X2': y2})

    # Test 1: check the type of the output
    # assert isinstance(ft.fourier_transform(data=my_df1,
    #                   time_col='X1',
    #                   data_col='X2'),
    #                   alt.vegalite.v3.api.Chart), \
    #     "Return type is not an Altair object!"

    # assert isinstance(ft.fourier_transform(data=my_df2,
    #                   time_col='X1',
    #                   data_col='X2'),
    #                   alt.vegalite.v3.api.Chart), \
    #     "Return type is not an Altair object!"

    # # Test 2: check if the output is a line chart
    # assert ft.fourier_transform(data=my_df1,
    #                             time_col='X1',
    #                             data_col='X2') == "line",\
    #     "Return plot should be a line plot!"
    # assert ft.fourier_transform(data=my_df2,
    #                             time_col='X1',
    #                             data_col='X2') == "line", \
    #     "Return plot should be a line plot!"
    
    # Test 3: check the data type of the x-axis mapping
    assert ft.fourier_transform(my_df1, 'X1', 'X2').to_dict()['encoding']['x'][
        'type'] == "quantitative", \
        "Plot x-axis should be of quantitative type!"

    assert ft.fourier_transform(my_df2, 'X1', 'X2').to_dict()['encoding']['x'][
        'type'] == "quantitative", \
        "Plot x-axis should be of quantitative type!"

    # Test 4: check the data type of the y-axis mapping
    assert ft.fourier_transform(my_df1, 'X1', 'X2').to_dict()['encoding']['y'][
        'type'] == "quantitative", \
        "Plot y-axis should be of quantitative type!"
    assert ft.fourier_transform(my_df2, 'X1', 'X2').to_dict()['encoding']['y'][
        'type'] == "quantitative", \
        "Plot y-axis should be of quantitative type!"

    return
