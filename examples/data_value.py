import numpy as np
import sys

from plotter import Plotter, PlotterType

to_plot = [
    {
        "title": "No data value",
        "type": PlotterType.BAR,
        "data": np.random.random(5)
    },
    {
        "title": "Default data value",
        "type": PlotterType.BAR,
        "data": np.random.random(5),
        "show_data_value": True
    },
    {
        "title": "Data value font size = 20 and color = #d34f73",
        "type": PlotterType.BAR,
        "data": np.random.random(5),
        "show_data_value": True,
        "data_value_fontsize": 20,
        "data_value_color": "#d34f73"
    },
]

pl = Plotter(to_plot)
pl.show()
