import pytest
import numpy as np
from altairexpress import altairexpress as ae
from gapminder import gapminder

# define testing data
gapminder


def test_hist(gapminder):
    # make histogram of input variable
    plot = hist(data=gapminder, variable='lifeExp')

    # convert  plot to dict object
    plot_dict = plot.to_dict()


    # ensure the layers have the expected marks
    assert plot_dict['layer'][0]['mark'] == 'bar'
    assert plot_dict['layer'][1]['mark']['type'] == 'rule'
    assert plot_dict['layer'][2]['mark']['type'] == 'rule'

    # check the layers have the correct encodings
    assert plot_dict['layer'][0]['encoding']['x']['type'] == 'quantitative'
    assert plot_dict['layer'][1]['encoding']['x']['type'] == 'quantitative'
    assert plot_dict['layer'][2]['encoding']['x']['type'] == 'quantitative'
    assert plot_dict['layer'][0]['encoding']['y']['aggregate'] == 'count'
    assert plot_dict['layer'][1]['encoding']['x']['aggregate'] == 'mean'
    assert plot_dict['layer'][2]['encoding']['x']['aggregate'] == 'median'

    return










