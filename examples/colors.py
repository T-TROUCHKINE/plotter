import numpy as np
import sys

from plotter import Plotter, PlotterType

to_plot = [
    {
        "title": "Default colors",
        "type": PlotterType.MULTIBAR,
        "data": [np.random.random(5), np.random.random(5)],
        "x_ticklabels": ["label {}".format(i) for i in range(5)],
        "bar_width": 0.4
    },
    {
        "title": "Custom colors",
        "type": PlotterType.MULTIBAR,
        "data": [np.random.random(5), np.random.random(5)],
        "x_ticklabels": ["label {}".format(i) for i in range(5)],
        "bar_width": 0.4,
        "colors": ["#70161e", "#1c3144"]
    },
]

pl = Plotter(to_plot)
pl.show()
