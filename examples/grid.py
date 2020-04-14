import numpy as np
import sys

from plotter import Plotter, PlotterType

x = np.linspace(-np.pi, np.pi, 201)

to_plot = [
    {
        "title": "No grid",
        "type": PlotterType.PLOT,
        "data": [x, np.sin(x)]
    },
    {
        "title": "With grid",
        "type": PlotterType.PLOT,
        "data": [x, np.sin(x)],
        "show_grid": True
    },
    {
        "title": "With X grid",
        "type": PlotterType.PLOT,
        "data": [x, np.sin(x)],
        "show_xgrid": True
    },
    {
        "title": "With Y grid",
        "type": PlotterType.PLOT,
        "data": [x, np.sin(x)],
        "show_ygrid": True
    },
]

pl = Plotter(to_plot)
pl.show()
