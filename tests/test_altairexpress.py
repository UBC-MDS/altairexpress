from altairexpress import altairexpress as ax
import pytest
import pandas as pd
import numpy as np


@pytest.fixture
def test_df1():
    data1 = "https://raw.github.ubc.ca/MDS-2019-20/DSCI_574_spat-temp-mod_students/master/labs/release/lab1/data/ts4_jjshares.csv?token=AAAAOMZQBS5IDU4Q6K3RBXS6NG7NM"
    return data1

def test_df2():
    df = pd.read_csv(test_df1())
    df2 = df.iloc[0, 1] = "a"
    data2 = df2.to_csv(index=False)
    return data2

def test_ts():
    # test the plot type is correct
    assert isinstance(ax.ts_alt(test_df1, "earnings", 4)), alt.vegalite.v3.api.Chart), "Plot type is not an Altair object."    
    assert ax.ts_alt(test_df1, "earnings", 4).to_dict()['mark'] == "line", "The plot should be line charts."
    
    # test the axes of the plot is correctly mapped
    assert ax.ts_alt(test_df1, "earnings", 4).to_dict()['encoding']['x']['field'] == 'date', "Plot x-axis ahould be mapped to date"
    assert ax.ts_alt(test_df1, "earnings", 4).to_dict()['encoding']['y']['field'] == 'value', "Plot y-axis ahould be mapped to value"

    # test the Exception is correctly raised
    with pytest.raises(Exception) as e:
        assert ax.ts_alt(123, "earnings", 4)
    assert str(e.value) == "TypeError: The path of the data must be entered as a string."

    with pytest.raises(Exception) as e:
        assert ax.ts_alt(test_df1, 2, 4)
    assert str(e.value) == "TypeError: The column name must be entered as a string."

    with pytest.raises(Exception) as e:
        assert ax.ts_alt(test_df1, "earnings", "4")
    assert str(e.value) == "TypeError: The frequency must be entered as an integer."

    with pytest.raises(Exception) as e:
        assert ax.ts_alt(test_df1, "earnings", 6)
    assert str(e.value) == "ValueError: Frequency must be 1/4/12/52."

    with pytest.raises(Exception) as e:
        assert ax.ts_alt(test_df1, "earning", 4)
    assert str(e.value) == "ValueError: The column name were not found in the original data."

    with pytest.raises(Exception) as e:
        assert ax.ts_alt(test_df1, "earning", 4)
    assert str(e.value) == "ValueError: The column name were not found in the original data."


