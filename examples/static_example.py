import sys
import numpy as np
import time

from plotter import Plotter


def build_test():
    matrix = np.random.randint(0, 10, (100, 100))
    scatter = [np.random.random(30), np.random.random(30)]
    scatter2 = np.random.random((50, 50))
    hist = np.random.random(100)
    hist2 = np.random.random(100)
    trace = np.random.random(500)
    bar = np.random.random(5)

    to_plot = [
        {
            "title": "Test matrix",
            "type": "matrix",
            "data": matrix,
            "x_label": "Abscissa",
            "y_label": "Orderly",
        },
        {
            "title": "Bars monitoring",
            "type": "bar",
            "data": bar,
            "x_label": "X axis",
            "y_label": None,
            "x_ticklabels": ["A", "B", "C", "D", "E"],
            "show_data_value": True,
            "data_value_color": "black",
            "rotate_x_label": True,
        },
        {
            "title": "Random scatter",
            "type": "scatter",
            "data": scatter,
            "x_label": None,
            "y_label": "Label",
        },
        {
            "title": "Some histogram",
            "type": "histogram",
            "data": [hist, hist2],
            "x_label": "The X axis",
            "y_label": "Some value",
        },
        {
            "title": "Side channel",
            "type": "trace",
            "data": trace,
            "x_label": "Time",
            "y_label": "Consumption",
        },
        {
            "title": "Scatter from matrix",
            "type": "scatter",
            "data": scatter2,
            "x_label": None,
            "y_label": None,
        },
    ]

    return to_plot


to_plot = build_test()
pl = Plotter(to_plot, figsuptitle="Dynamic example")
pl.show()
