import numpy as np
import sys

from plotter import Plotter, PlotterType

x = np.linspace(-np.pi, np.pi, 201)

to_plot = [
    {
        "title": "Default labels",
        "type": PlotterType.PLOT,
        "data": [x, np.sin(x)]
    },
    {
        "title": "Custom labels with default font size",
        "type": PlotterType.PLOT,
        "data": [x, np.sin(x)],
        "x_label": "X LABEL",
        "y_label": "Y LABEL"
    },
    {
        "title": "Custom labels and font sizes",
        "type": PlotterType.PLOT,
        "data": [x, np.sin(x)],
        "x_label": "X LABEL",
        "y_label": "Y LABEL",
        "x_label_fontsize": 20,
        "y_label_fontsize": 8
    },
    {
        "title": "Labels on a pie",
        "type": "pie",
        "data": np.random.randint(100, size=5),
        "labels": ["data{}".format(i) for i in range(5)]
    }
]

pl = Plotter(to_plot)
pl.show()
