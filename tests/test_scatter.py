# test_scatter.py
import pytest
from vega_datasets import data
import pandas as pd
import numpy as np
from altairexpress import scatter as sc

@pytest.fixture
def test_df():
    test_data = data.cars()
    return test_data

@pytest.fixture
def test_negative():
    negative_data = pd.DataFrame({"x":[1,2,6,7,83,-1], "y": [1,25,6,-77,2,3]})
    return negative_data

def test_scatter(test_df):


    # example 1
    plot = sc.make_scatter(test_df, xval = "Horsepower", yval = "Acceleration")
    plot_dict = plot.to_dict()

    # make sure the right marks are used in altair
    assert plot_dict['vconcat'][0]['mark']['type'] == "bar"
    assert plot_dict['vconcat'][1]['hconcat'][0]['mark']['type'] == "circle"
    assert plot_dict['vconcat'][1]['hconcat'][1]['mark']['type'] == "bar"

    # ensure all variables are quantitative
    assert plot_dict['vconcat'][0]['encoding']['x']['type'] == "quantitative"
    assert plot_dict['vconcat'][0]['encoding']['y']['type'] == "quantitative"
    assert plot_dict['vconcat'][1]['hconcat'][0]['encoding']['x']['type'] == "quantitative"
    assert plot_dict['vconcat'][1]['hconcat'][0]['encoding']['y']['type'] == "quantitative"
    assert plot_dict['vconcat'][1]['hconcat'][1]['encoding']['x']['type'] == "quantitative"
    assert plot_dict['vconcat'][1]['hconcat'][1]['encoding']['y']['type'] == "quantitative"

    # example 2
    plot_two = sc.make_scatter(test_df, xval = "Displacement", yval = "Weight_in_lbs", x_transform = True, y_transform = True)
    plot_dict = plot_two.to_dict()

    # ensure proper domains are being established after transforming the data.
    assert np.log(test_df['Displacement']).min() == plot_dict['vconcat'][1]['hconcat'][0]['encoding']['x']['scale']['domain'][0]
    assert np.log(test_df['Displacement']).max() == plot_dict['vconcat'][1]['hconcat'][0]['encoding']['x']['scale']['domain'][1]

    assert np.log(test_df['Weight_in_lbs']).min() == plot_dict['vconcat'][1]['hconcat'][0]['encoding']['y']['scale']['domain'][0]
    assert np.log(test_df['Weight_in_lbs']).max() == plot_dict['vconcat'][1]['hconcat'][0]['encoding']['y']['scale']['domain'][1]

    return 

# Test all errors and warning branches
def test_errors(test_df):
    with pytest.raises(ValueError):
        sc.make_scatter(test_df, xval = "Horse", yval = "Acceleration")

def test_negX(test_negative):
    with pytest.warns(UserWarning):
        sc.make_scatter(test_negative, xval = "x", yval = "y", x_transform = True)

def test_negY(test_negative):
    with pytest.warns(UserWarning):
        sc.make_scatter(test_negative, xval = "x", yval = "y", y_transform = True)
