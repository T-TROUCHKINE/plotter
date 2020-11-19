---
layout: page
title: Basic usage of Plotter
permalink: /bases/
nav_order: 2
---
# Basic usage of Plotter
This page presents the bases for using Plotter.

The Plotter library is built to use a descriptive view of the figure we want to
plot. The figure is described with a list of dictionaries (usually named the
`to_plot` variable). A dictionary contains every information needed for the
`Plotter` class to plot the desired figure. When more than one dictionaries are
in the list, they will plot sub-figures. The `Plotter` class must be set with
something to plot before calling any of its function.

A classical Plotter program looks like:
```python
from plotter import Plotter

to_plot = [dict0, dict1, dict2, ...]

pl = Plotter(to_plot)
# Do something with pl
```

Currently there are three actions available with the `Plotter` class:
- plot the figure(s)
- dynamically plot the figure(s)
- export the figure(s) in Tikz

## Plot the figures
Plotting the figures can simply be done by calling the `show()` method.

### Example
```python
import numpy as np
from plotter import Plotter

x = np.linspace(-np.pi, np.pi, 200)

to_plot = [{
    "title": "Example",
    "type": "plot",
    "data": [x, np.sin(x)]
}]

pl = Plotter(to_plot)
pl.show()
```

In this case, the Plotter will display a figure representing the points (x,
sin(x)) for x in -Pi and Pi with a resolution of 200 points. The `data` key
contains the table with the X values and the Y values, the `type` key contains
the style to use for plotting these data (more information
[here]({{baseurl}}/types/)) and the `title` key contains the title of the
figure.

### Result
![First plot result](/img/ex1.png)

## Dynamic plot
The dynamic plot can be done using the `show()` method with the `blocking=False` argument in a loop.

### Example
```python
import numpy as np
from plotter import Plotter

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
```

In this example, the Y values are regularly recomputed and the `to_plot`
attribute of the `Plotter` class is updated and the figure is also updated.

## Export figure to Tikz
It is possible to export the figure into a Tikz file using `export_tikz()`
method. The `filename` argument can be given to export the figure into a
specific file, by default the filename is `tikz_figure.tex`.

### Example
```python
import numpy as np
from plotter import Plotter

x = np.linspace(-np.pi, np.pi, 200)

to_plot = [{
    "title": "Example",
    "type": "plot",
    "data": [x, np.sin(x)]
}]

pl = Plotter(to_plot)
pl.export_tikz()
```

## `Plotter` arguments
The `Plotter` class supports other arguments that can be passed to customize or adapt the figure.

| Argument        | Type                                                                                           | Description                                                                                                                            | Default value |
| :-----          | :----                                                                                          | :---                                                                                                                                   | :--           |
| figsuptitle     | `str`                                                                                          | This argument is the global title of the figures.                                                                                      | `None`        |
| figsize         | `tuple`                                                                                        | This argument is the size of the window containing the figures.                                                                        | `(20,20)`     |
| tikz_file       | `str`                                                                                          | This argument is the default used name for the file storing the Tikz code when exporting the figure into Tikz                          | `""`          |
| cmap            | `Matplotlib cmap Object` ([Doc](https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html)) | This argument is the used color-map for the Plots                                                                                      | `plt.cm.jet`  |
| latex           | `bool`                                                                                         | This argument is a flag setting or not the support of Latex commands and fonts ([Doc](https://matplotlib.org/1.3.1/users/usetex.html)) | `False`       |
| force_stack_dir | `str` among `"v"` or `"h"`                                                                     | This argument describes the orientation of the stacking of the sub-figures                                                             | `None`         |

Now that you know how to use the `Plotter` class, you should check out how to create a dictionary for a figure.

<span class="fs-4">
[Figure dictionnaries >>]({{site.baseurl}}/dict/){: .btn}
</span>
