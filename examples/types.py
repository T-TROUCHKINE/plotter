import sys
import numpy as np
import time

from plotter import Plotter

x = np.linspace(-np.pi, np.pi, 201)

to_plot = [
    {
        "title": "Multiplot",
        "type": "multiplot",
        "data": [[10,11,12,13,14,15,16],[[3,4,5,8,4,6,4],[0,5,6,8,7,4,3]]],
        "marker": "-o"
    },
    {
        "title": "Plot with markers",
        "type": "plot",
        "data": [[10,11,12,13,14,15,16],[3,4,5,8,4,6,4]],
        "marker": "-o"
    },
    {
        "title": "Plot",
        "type": "plot",
        "data": [x, np.sin(x)],
    },
    {
        "title": "Matrix",
        "type": "matrix",
        "data": np.random.randint(0, 10, (100, 100)),
    },
    {
        "title": "Bar",
        "type": "bar",
        "data": np.random.random(5),
    },
    {
        "title": "Scatter",
        "type": "scatter",
        "data": np.random.random((50,50)),
    },
    {
        "title": "Histogram",
        "type": "histogram",
        "data": [np.random.random(100), np.random.random(100)],
    },
    {
        "title": "Trace",
        "type": "trace",
        "data": np.random.random(500),
    },
    {
        "title": "Multiple Traces",
        "type": "multitrace",
        "data": [np.random.random(500), np.random.random(500)],
    },
    {
        "title": "Multiple Bars",
        "type": "multibar",
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
        "type": "pie",
        "data": np.random.randint(100, size=5)
    },
    {
        "title": "Multiple Scatter",
        "type": "multiscatter",
        "data": [np.random.random((50,50)), np.random.random((50,50))],
    },
    {
        "title": "Matrix Scatter",
        "type": "matrixscatter",
        "data": np.random.randint(0, 10, (40, 40))
    },
    {
        "title": "Multiple matrix scatter binary",
        "type": "multimatrixscatterbin",
        "data": [np.matrix([[0,1,0,0],[7,1,2,0],[0,0,2,0],[0,1,0,0]]),
                 np.matrix([[1,0,4,4],[0,0,0,3],[7,0,0,1],[4,0,0,8]])]
    },
]

pl = Plotter(to_plot)
pl.show()
