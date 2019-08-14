import numpy as np
import sys

from plotter import Plotter, PlotterType

x = np.linspace(0.1, 100, 201)

to_plot = [
    {
        "title": "Standard positioning",
        "type": PlotterType.PLOT,
        "data": [x, np.log(x)],
        "x_ticklabels": ["{}".format(i) for i in range(int(min(x)), int(max(x)), 10)],
        "x_ticklabels_position": [i for i in range( int(min(x)), int(max(x)), 10)],
    },
    {
        "title": "Custom positioning (exponentially)",
        "type": PlotterType.PLOT,
        "data": [x, x],
        "x_ticklabels": ["{}".format(i) for i in range(int(min(x)), int(max(x)), 10)],
        "x_ticklabels_position": [i for i in range( int(min(x)), int(max(x)), 10)],
        "y_ticklabels": ["{}".format(i) for i in range(100)],
        "y_ticklabels_position": [np.exp(i) for i in range(100)]
    }
]

pl = Plotter(to_plot)
pl.show()
