from altairexpress import altairexpress as ax
import pytest
# import pandas as pd
# import numpy as np
import altair as alt


def test_ts():
    """
    Tests the time series function ts_alt to make sure the outputs are
    correctly rendering.
    Returns:
    --------
    None
        The test should pass and no asserts should be displayed.
    """
    test_df1 = "https://raw.github.ubc.ca/MDS-2019-20/DSCI_574_spat-temp-\
mod_students/master/labs/release/lab1/data/ts4_jjshares.csv?token=\
AAAAOMZQBS5IDU4Q6K3RBXS6NG7NM"
    test_df2 = "https://raw.github.ubc.ca/MDS-2019-20/DSCI_574_spat-temp-\
mod_students/master/labs/release/lab1/data/ts1_globaltemp.csv?token=\
AAAAOM4GFOSICJVSVP2YUP26NG7QE"
    # test the plot type is correct
    # assert isinstance(ax.ts_alt(test_df1, "earnings", 4),
    #                   alt.vegalite.v3.api.Chart), \
    #     "Plot type is not an Altair object."
    # assert isinstance(ax.ts_alt(test_df2, "temp", 1),
    #                   alt.vegalite.v3.api.Chart), \
    #     "Plot type is not an Altair object."
    assert ax.ts_alt(test_df1, "earnings", 4).to_dict()[
                     'mark'] == "line", "The plot should be line charts."
    assert ax.ts_alt(test_df2, "temp", 1).to_dict()[
                     'mark'] == "line", "The plot should be line charts."

    # test the axes of the plot is correctly mapped
    assert ax.ts_alt(test_df1, "earnings", 4).to_dict()[
                     'encoding']['x']['field'] == 'date', "Plot x-axis ahould \
                         be mapped to date"
    assert ax.ts_alt(test_df1, "earnings", 4).to_dict()[
                     'encoding']['y']['field'] == 'value', "Plot y-axis ahould \
                         be mapped to value"
    assert ax.ts_alt(test_df2, "temp", 1).to_dict()[
                     'encoding']['x']['field'] == 'year', "Plot x-axis ahould \
                         be mapped to date"
    assert ax.ts_alt(test_df2, "temp", 1).to_dict()[
                     'encoding']['y']['field'] == 'temp', "Plot y-axis ahould \
                         be mapped to value"

    # test the Exception is correctly raised
    with pytest.raises(Exception) as e:
        assert ax.ts_alt(123, "earnings", 4)
    assert str(
        e.value) == "TypeError: The path of the data must be entered as a \
string."

    with pytest.raises(Exception) as e:
        assert ax.ts_alt(test_df1, 2, 4)
    assert str(
        e.value) == "TypeError: The column name must be entered as a string."

    with pytest.raises(Exception) as e:
        assert ax.ts_alt(test_df1, "earnings", "4")
    assert str(
        e.value) == "ValueError: Frequency must be an integer from {1, 4, 12, \
52}."

    with pytest.raises(Exception) as e:
        assert ax.ts_alt(test_df1, "earnings", 6)
    assert str(
        e.value) == "ValueError: Frequency must be an integer from {1, 4, 12, \
52}."

    with pytest.raises(Exception) as e:
        assert ax.ts_alt(test_df1, "earning", 4)
    assert str(
        e.value) == "ValueError: The column name were not found in the \
original data."
