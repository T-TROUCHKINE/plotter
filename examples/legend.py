import numpy as np
import sys

from plotter import Plotter, PlotterType

to_plot = [
    {
        "title": "No legend",
        "type": PlotterType.MULTIBAR,
        "data": [np.random.random(5),np.random.random(5)],
        "x_ticklabels": ["label {}".format(i) for i in range(5)],
        "bar_width": 0.4
    },
    {
        "title": "Legend",
        "type": PlotterType.MULTIBAR,
        "data": [np.random.random(5),np.random.random(5)],
        "x_ticklabels": ["label {}".format(i) for i in range(5)],
        "bar_width": 0.4,
        "legend": ["Set 1", "Set 2"]
    },
]

pl = Plotter(to_plot)
pl.show()
