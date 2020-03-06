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

def test_scatter(test_df):

    # check axis; are the variables numeric
    # check axis of the plot itself
    # check the mark
    # example 1
    plot = sc.make_scatter(test_df, xval = "Horsepower", yval = "Acceleration")
    plot_dict = plot.to_dict()

    assert plot_dict['vconcat'][0]['mark']['type'] == "bar"
    assert plot_dict['vconcat'][1]['hconcat'][0]['mark']['type'] == "circle"
    assert plot_dict['vconcat'][1]['hconcat'][1]['mark']['type'] == "bar"


    assert plot_dict['vconcat'][0]['encoding']['x']['type'] == "quantitative"
    assert plot_dict['vconcat'][0]['encoding']['y']['type'] == "quantitative"
    assert plot_dict['vconcat'][1]['hconcat'][0]['encoding']['x']['type'] == "quantitative"
    assert plot_dict['vconcat'][1]['hconcat'][0]['encoding']['y']['type'] == "quantitative"
    assert plot_dict['vconcat'][1]['hconcat'][1]['encoding']['x']['type'] == "quantitative"
    assert plot_dict['vconcat'][1]['hconcat'][1]['encoding']['y']['type'] == "quantitative"

    # example 2
    plot_two = sc.make_scatter(test_df, xval = "Displacement", yval = "Weight_in_lbs", x_transform = True, y_transform = True)
    plot_dict = plot_two.to_dict()

    assert np.log(test_df['Displacement']).min() == plot_dict['vconcat'][1]['hconcat'][0]['encoding']['x']['scale']['domain'][0]
    assert np.log(test_df['Displacement']).max() == plot_dict['vconcat'][1]['hconcat'][0]['encoding']['x']['scale']['domain'][1]

    assert np.log(test_df['Weight_in_lbs']).min() == plot_dict['vconcat'][1]['hconcat'][0]['encoding']['y']['scale']['domain'][0]
    assert np.log(test_df['Weight_in_lbs']).max() == plot_dict['vconcat'][1]['hconcat'][0]['encoding']['y']['scale']['domain'][1]

    return 

#assert whether an error is raised or not.
#dir()
#check for quantitative variables

