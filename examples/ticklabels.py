import numpy as np

from plotter import Plotter, PlotterType

x = np.linspace(-np.pi, np.pi, 201)

to_plot = [
    {
        "title": "Default x tick labels",
        "type": PlotterType.BAR,
        "data": np.random.random(5)
    },
    {
        "title": "Custom x tick labels",
        "type": PlotterType.BAR,
        "data": np.random.random(5),
        "x_ticklabels": ["label {}".format(i) for i in range(5)]
    },
    {
        "title": "Custom tick labels for matrix scatter",
        "type": PlotterType.MATRIXSCATTER,
        "data": np.random.randint(0, 10, (20,20)),
        "x_ticklabels": ["X{}".format(i) for i in range(20)],
        "y_ticklabels": ["Y{}".format(i) for i in range(20)],
    }
]

pl = Plotter(to_plot)
pl.show()
