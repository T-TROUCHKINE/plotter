import numpy as np
import sys

from plotter import Plotter

x = np.linspace(-np.pi, np.pi, 201)

to_plot = [
    {"title": "Example 1", "type": "plot", "data": [x, np.sin(x)]},
    {"title": "Example 2", "type": "matrix", "data": np.random.random((100, 100))},
]

pl = Plotter(to_plot, figsuptitle="Multi-plot")
pl.show()
