import numpy as np
import sys

from plotter import Plotter, PlotterType

to_plot = [
    {
        "title": "Default colorbar font size",
        "type": PlotterType.MATRIX,
        "data": np.random.randint(0, 10, (100, 100)),
    },
    {
        "title": "Colorbar font size = 20",
        "type": PlotterType.MATRIX,
        "data": np.random.randint(0, 10, (100, 100)),
        "colorbar_fontsize": 20
    },
]

pl = Plotter(to_plot)
pl.show()
