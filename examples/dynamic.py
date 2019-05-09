import sys
import numpy as np
import time

from plotter import Plotter, PlotterType

NB_PTS = 200

def build_to_plot(i):
    x = np.linspace(-np.pi, np.pi, NB_PTS)
    to_plot = [
        {
            "title": "Dynamic Plot",
            "type": PlotterType.PLOT,
            "data": [x, np.sin(x+(i/NB_PTS))],
        },
    ]
    return to_plot

i = 0
to_plot = build_to_plot(i)
pl = Plotter(to_plot)
while 1:
    i+=30
    pl.set_to_plot(build_to_plot(i))
    pl.show(blocking=False)
