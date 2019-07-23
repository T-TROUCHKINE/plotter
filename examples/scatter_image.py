import numpy as np

from plotter import Plotter

to_plot = [
    {
        "title": "Matrix Scatter with matrix scale to image",
        "type": "matrixscatter",
        "data": np.random.randint(0, 10, (20, 20)),
        "image": "img/usa.jpg",
        "revert_y_axis": True,
        "scale_to_image": True
    },
    {
        "title": "Multi Scatter",
        "type": "multiscatter",
        "data": [np.random.randint(0, 1000, (100,100)), np.random.randint(0, 1000, (100,100))],
        "image": "img/usa.jpg",
        "revert_y_axis": True
    },
    {
        "title": "Scatter",
        "type": "multiscatter",
        "data": [np.random.randint(0, 1000, (100,100))],
        "image": "img/usa.jpg",
        "revert_y_axis": True
    }
]

pl = Plotter(to_plot)
pl.show()
