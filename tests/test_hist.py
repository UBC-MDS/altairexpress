from altairexpress import hist as ae
from gapminder import gapminder
from pytest import raises


def test_hist():
    # define testing data
    gapminder

    # make histogram of input variable
    plot = ae.hist(data=gapminder, variable='lifeExp')

    # check that exception is raised when input is incorrect type
    with raises(TypeError):
        ae.hist(data={'column1:[1,2,3,3]'}, variable="column1")

    # check that exception is raised when variable is not of type string
    # TODO running this test leads to failing PEP8 since lifeExp not defined
    # with raises(TypeError):
    # ae.hist(data=gapminder, variable=lifeExp)

    # check that exception raised when variable is non-numeric
    with raises(TypeError):
        ae.hist(data=gapminder, variable='country')

    # check exception is raised when variable not contained in data
    with raises(NameError):
        ae.hist(data=gapminder, variable='passion')

    # convert plot to dict object
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

    # check the annotation text
    assert plot_dict[plot_dict['layer'][1]['mark']['text']] == 'Mean is 59.47'
    assert plot_dict[plot_dict['layer'][1]['mark']['text']] == 'Median is ' \
                                                               '60.71 '

    return
