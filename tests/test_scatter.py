# test_scatter.py
import pytest
from vega_datasets import data
import pandas as pd
from altairexpress import scatter

@pytest.fixture
def test_df():
    test_data = data.cars()
    return test_data

def test_scatter(test_df):

    # check axis; are the variables numeric
    # check axis of the plot itself
    # check the mark
    return (print("nothing yet"))

#assert whether an error is raised or not.