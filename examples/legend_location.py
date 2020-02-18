from plotter import Plotter
import numpy as np

""" See https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.legend.html
for getting possible legend locations. """

tp = [
    {
        "title": "Natural legend position",
        "type": "trace",
        "data": np.random.randint(0,10,1000),
        "legend": ["A trace"]
    },
    {
        "title": "Forced legend position",
        "type": "trace",
        "data": np.random.randint(0,10,1000),
        "legend": ["A trace"],
        "legend_location": "upper right"
    }
]

pl = Plotter(tp)
pl.show()
