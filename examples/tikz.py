import numpy as np
import sys

from plotter import Plotter, PlotterType

x = np.linspace(-np.pi, np.pi, 201)

to_plot = [
    {
        "title": "Plot",
        "type": PlotterType.PLOT,
        "data": [x, np.sin(x)]
    },
]

pl = Plotter(to_plot)
pl.export_tikz(filename="tikz/tikz_figure.tex")
