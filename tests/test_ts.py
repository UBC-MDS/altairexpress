from altairexpress import ts
import pytest
import altair as alt
import pandas as pd


@pytest.fixture
def test_ts():
    """
    Tests the time series function ts_alt to make sure the outputs are
    correctly rendering.
    Returns:
    --------
    None
        The test should pass and no asserts should be displayed.
    """
    time = ["1950 Q1", "1950 Q2", "1950 Q3",
            "1950 Q4", "1951 Q1", "1951 Q2",
            "1951 Q3", "1951 Q4"]
    earnings = [0.71, 0.63, 0.82, 0.91, 0.71, 0.63, 0.82, 0.91]
    ts_data = pd.DataFrame({'time': time, 'earnings': earnings})
    test_plot = ts.ts_alt(data=ts_data, col="earnings", frequency=4)

    year = ["1950", "1951", "1952", "1953",
            "1954", "1955", "1956", "1957"]
    temp = [0.71, 0.63, 0.82, 0.91, 0.51, 1.31, 1.82, 2.01]
    ts_data2 = pd.DataFrame({'year': year, 'temp': temp})
    test_plot2 = ts.ts_alt(ts_data2, "temp", 1)

    # test the plot type is correct
    assert isinstance(test_plot,
                      alt.vegalite.v3.api.Chart), \
        "Plot type is not an Altair object."
    assert isinstance(test_plot2,
                      alt.vegalite.v3.api.Chart), \
        "Plot type is not an Altair object."
    assert test_plot.to_dict()[
                     'mark'] == "line", "The plot should be line charts."
    assert test_plot2.to_dict()[
                     'mark'] == "line", "The plot should be line charts."

    # test the axes of the plot is correctly mapped
    assert test_plot.to_dict()[
                     'encoding']['x']['field'] == 'date', "Plot x-axis ahould \
                         be mapped to date"
    assert test_plot.to_dict()[
                     'encoding']['y']['field'] == 'value', "Plot y-axis ahould \
                         be mapped to value"
    assert test_plot2.to_dict()[
                     'encoding']['x']['field'] == 'year', "Plot x-axis ahould \
                         be mapped to date"
    assert test_plot2.to_dict()[
                     'encoding']['y']['field'] == 'temp', "Plot y-axis ahould \
                         be mapped to value"

    # test the Exception is correctly raised
    with pytest.raises(Exception) as e:
        assert ts.ts_alt(123, "earnings", 4)
    assert str(
        e.value) == "TypeError: The path of the data must be entered as a \
            string."

    with pytest.raises(Exception) as e:
        assert ts.ts_alt(ts_data, 2, 4)
    assert str(
        e.value) == "TypeError: The column name must be entered as a string."

    with pytest.raises(Exception) as e:
        assert ts.ts_alt(ts_data, "earnings", "4")
    assert str(
        e.value) == "ValueError: Frequency must be an integer from {1, 4, 12, \
            52}."

    with pytest.raises(Exception) as e:
        assert ts.ts_alt(ts_data, "earnings", 6)
    assert str(
        e.value) == "ValueError: Frequency must be an integer from {1, 4, 12, \
            52}."

    with pytest.raises(Exception) as e:
        assert ts.ts_alt(ts_data, "earning", 4)
    assert str(
        e.value) == "ValueError: The column name were not found in the \
            original data."
    return
