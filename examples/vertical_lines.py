import numpy as np
import sys

from plotter import Plotter, PlotterType

x = np.linspace(-np.pi, np.pi, 201)

to_plot = [
    {
        "title": "Plot",
        "type": PlotterType.PLOT,
        "data": [x, np.sin(x)],
        "vlines": [-0.3,1.2],
        "vline_color": ["darkgrey"]
    },
]

pl = Plotter(to_plot)
pl.show()
