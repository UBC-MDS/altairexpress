## altairexpress 

![](https://github.com/aromatic-toast/altairexpress/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/aromatic-toast/altairexpress/branch/master/graph/badge.svg)](https://codecov.io/gh/aromatic-toast/altairexpress) ![Release](https://github.com/aromatic-toast/altairexpress/workflows/Release/badge.svg)

[![Documentation Status](https://readthedocs.org/projects/altairexpress/badge/?version=latest)](https://altairexpress.readthedocs.io/en/latest/?badge=latest)

Python package that creates basic EDA graphics in Altair with ease.

### Installation:

```
pip install -i https://test.pypi.org/simple/altairexpress
```

### Summary Overview
- This package aims to simplify the process of conducting EDA on new datasets. We have designed some functions that allows us to do basic data manipulation and plotting, all by writing only one line of code. Plotting will be done using the Altair package. As Jenny Bryan once said: “Someone has to write for-loops, but it doesn’t have to be you!”. We are essentially implementing this mentality into EDA analysis. The user will be able to spend more time on analyzing his or her dataset and less time configuring Altair settings. 

### Features
- **Fast Fourier transforms:** We feel that this function is missing from many summary functions and can be really useful for some cases. The user will be able to input time series data and the function will automatically implement frequency analysis and provide a frequency vs amplitude plot.

- **Scatter plot:** Here we will take our own spin on 2-d scatter plots. We feel that the it is often the case that we don’t know the distribution of the given points. This is why this function will group the points by each of the x and y axes and provide two histograms alongside the scatter plot. This way, the user will have greater intuition on the properties of the data.

- **Bar chart:** We will create a function that takes 1-d data and create a bar chart of It using Altair. However, we will also provide summary statistics as well as plot them (e.g. mean and median lines) as overlaying lines.


- **Time series analysis:** We will create a function to decompose time series data and plot the components. The 4 plots are: raw data, estimated trend component, estimated seasonal/cyclic component and residual component.


### Dependencies

- [Altair](https://altair-viz.github.io)
- [Numpy](https://numpy.org)

### Usage

- Although what our package does is by no means ‘new’ from a technical perspective (we are relying on already built packages to do everything), it does provide convenience to the user. There are many more universal summary packages out there, such as [pandas.DataFrame.describe()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html) for python and [summary](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/summary) for R), our package is able to combine both analysis and visual representation of the data for specific (FFT) and general (bar chart) tasks.

### Documentation
The official documentation is hosted on Read the Docs: <https://altairexpress.readthedocs.io/en/latest/>

### Credits
This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
