import numpy as np
import sys

from plotter import Plotter, PlotterType

x = np.linspace(-np.pi, np.pi, 201)

to_plot = [
    {
        "title": "Plot with text added at an arbitrary position",
        "type": PlotterType.PLOT,
        "data": [x, np.sin(x)],
        "text": [(-0.5,0.75,"I am a text !"),(0,-1,"I am another one !")]
    },
]

pl = Plotter(to_plot)
pl.show()
