import numpy as np
import sys

from plotter import Plotter, PlotterType

to_plot = [
    {
        "title": "No x label rotation",
        "type": PlotterType.BAR,
        "data": np.random.random(5),
        "x_ticklabels": ["label {}".format(i) for i in range(5)]
    },
    {
        "title": "With x label rotation",
        "type": PlotterType.BAR,
        "data": np.random.random(5),
        "x_ticklabels": ["label {}".format(i) for i in range(5)],
        "rotate_x_labels": True
    },
]

pl = Plotter(to_plot)
pl.show()
