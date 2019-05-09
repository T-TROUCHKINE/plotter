import numpy as np
import sys

from plotter import Plotter, PlotterType

to_plot = [
    {
        "title": "Default x tick labels",
        "type": PlotterType.BAR,
        "data": np.random.random(5)
    },
    {
        "title": "Custom x tick labels",
        "type": PlotterType.BAR,
        "data": np.random.random(5),
        "x_ticklabels": ["label {}".format(i) for i in range(5)]
    },
]

pl = Plotter(to_plot)
pl.show()
