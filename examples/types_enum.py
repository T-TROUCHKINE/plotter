import sys
import numpy as np
import time

from plotter import Plotter, PlotterType

x = np.linspace(-np.pi, np.pi, 201)

to_plot = [
    {
        "title": "Plot with markers",
        "type": PlotterType.PLOT,
        "data": [[10,11,12,13,14,15,16],[3,4,5,8,4,6,4]],
        "marker": "-o"
    },
    {
        "title": "Plot",
        "type": PlotterType.PLOT,
        "data": [x, np.sin(x)],
    },
    {
        "title": "Matrix",
        "type": PlotterType.MATRIX,
        "data": np.random.randint(0, 10, (100, 100)),
    },
    {
        "title": "Bar",
        "type": PlotterType.BAR,
        "data": np.random.random(5),
    },
    {
        "title": "Scatter",
        "type": PlotterType.SCATTER,
        "data": np.random.random((50,50)),
    },
    {
        "title": "Histogram",
        "type": PlotterType.HISTOGRAM,
        "data": [np.random.random(100), np.random.random(100)],
    },
    {
        "title": "Trace",
        "type": PlotterType.TRACE,
        "data": np.random.random(500),
    },
    {
        "title": "Multiple Traces",
        "type": PlotterType.MULTITRACE,
        "data": [np.random.random(500), np.random.random(500)],
    },
    {
        "title": "Multiple Bars",
        "type": PlotterType.MULTIBAR,
        "data": [np.random.random(5), np.random.random(5)],
        "x_ticklabels": list(np.arange(0,5)),
        "bar_width": 0.3,
    },
    {
        "title": "Stacked Bars",
        "type": "stackedbar",
        "data": [np.random.random(5), np.random.random(5)]
    },
    {
        "title": "Pie",
        "type": PlotterType.PIE,
        "data": np.random.randint(100, size=5)
    },
    {
        "title": "Multiple Scatter",
        "type": PlotterType.MULTISCATTER,
        "data": [np.random.random((50,50)), np.random.random((50,50))],
    },
    {
        "title": "Matrix Scatter",
        "type": PlotterType.MATRIXSCATTER,
        "data": np.random.randint(0, 10, (40, 40))
    }
]

pl = Plotter(to_plot)
pl.show()
