## altairexpress 

![build](https://github.com/UBC-MDS/altairexpress/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/UBC-MDS/altairexpress/branch/master/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/altairexpress) ![Release](https://github.com/UBC-MDS/altairexpress/workflows/Release/badge.svg)

[![Documentation Status](https://readthedocs.org/projects/altairexpress/badge/?version=latest)](https://altairexpress.readthedocs.io/en/latest/?badge=latest)

Python package that creates basic EDA graphics in Altair with ease. It allows users to quickly create plots to facilitate exploratory data analysis along with providing additional summary statistics about the data such as mean, median, and correlation.

### Installation:

```
pip install -i https://test.pypi.org/simple/altairexpress
```

### Summary Overview
-  This package simplifies the process of conducting Exploratory Data Analysis (EDA) on new datasets. It is designed to allow the user to explore the data graphically as well as obtain some basic summary statistics, all by writing only one line of code. Plots are produced using the `Altair` package under the hood. As Jenny Bryan once said: “Someone has to write for-loops, but it doesn’t have to be you!”. This sentiment has been implemented here for EDA analysis. The user is able to spend more time on analyzing the dataset and less time on configuring complex Altair plot settings.

### Features
- **Fast Fourier transforms:** This function is missing from many summary functions and can be really useful for some cases. The user will be able to input time series data and the function will automatically implement frequency analysis and provide a frequency vs amplitude plot.

- **Scatter plot:** Here you will take your own spin on 2-d scatter plots. It is often the case that we don’t know the distribution of the given points. This is why this function will group the points by each of the x and y axes and provide two histograms alongside the scatter plot. This way, you will have greater intuition on the properties of the data.

- **Histogram:** This function takes in a dataframe and column name and creates a histogram. In addition, summary statistics of the input variable are overlayed onto the plot (e.g. mean and median vertical lines) and the sample standard deviation.


- **Time series analysis:** This is a function that takes in a local path to the time series data, decomposes the timeseries and finally visualizes the raw data along with decomposition components. Except annual time series, the function will return a graph with 4 subplots, which includes the raw data, estimated trend, seasonal/cyclic and noise components.


### Dependencies

- [Altair (v3.3.0 or higher)](https://altair-viz.github.io)
- [Numpy (v1.18.1 or higher)](https://numpy.org)

### How the package fits into the Python ecosytem

- Although what our package does is by no means ‘new’ from a technical perspective (we are relying on already built packages to do everything), it does provide convenience to the user. There are many more universal summary packages out there, such as [pandas.DataFrame.describe()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html) for python and [summary](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/summary) for R), our package is able to combine both analysis and visual representation of the data for specific (FFT) and general (bar chart) tasks.

### Documentation
The official documentation is hosted on Read the Docs: <https://altairexpress.readthedocs.io/en/latest/>

## Usage

```
from gapminder import gapminder
from altairexpress import hist
gapminder.head()
altairexpress.hist(gapminder, gdpPerCap)
```

```
from altairexpress import fourier_transform
my_data = pd.DataFrame(data = {'time_series': [0, 1, 2, 3],
                                       'signal': [2, 3, 4, 6]})
altairexpress.fourier_transform(data = my_data,
                                        time_col = 'time_series',
                                        data_col = 'signal')
```

### Credits
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
