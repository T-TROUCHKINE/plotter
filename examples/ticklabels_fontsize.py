import numpy as np
import sys

from plotter import Plotter, PlotterType

x = np.linspace(-np.pi, np.pi, 201)

to_plot = [
    {
        "title": "Default tick labels font size",
        "type": PlotterType.PLOT,
        "data": [x, np.sin(x)]
    },
    {
        "title": "Same custom tick labels font size",
        "type": PlotterType.PLOT,
        "data": [x, np.sin(x)],
        "ticklabels_fontsize": 20
    },
    {
        "title": "Different custom tick labels font size",
        "type": PlotterType.PLOT,
        "data": [x, np.sin(x)],
        "x_ticklabels_fontsize": 20,
        "y_ticklabels_fontsize": 8
    },
]

pl = Plotter(to_plot)
pl.show()
