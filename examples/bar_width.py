import numpy as np
import sys

from plotter import Plotter, PlotterType

to_plot = [
    {
        "title": "Bar width = 0.8 (default)",
        "type": PlotterType.BAR,
        "data": np.random.random(5)
    },
    {
        "title": "Bar width = 0.5",
        "type": PlotterType.BAR,
        "data": np.random.random(5),
        "bar_width": 0.5
    },
]

pl = Plotter(to_plot)
pl.show()
