---
layout: page
title: Plot data types
permalink: /types/
has_children: true
nav_order: 4
---
# Plot data types
This page presents the different ways of plotting data supported by Plotter and
how to use them.

## `PlotterType` class
The `PlotterType` class is an `Enum` which contains all plot styles. It is useful to list all available types.

### Example
```python
from Plotter import PlotterType

for t in PlotterType:
    print(t)
```
It also can be used as a `type` value in a dictionary.

### Example
```python
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.PLOT,
        "data": [[0,1,2,3,4,5], [15,6,5,3,5,8]]
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
![Minimal parameters plot](/img/ex2.png)

## Available types

| Type              | `PlotterType`   | Description                                                                                          | Data format                                                            |
| :---              | :-----          | :-----                                                                                               | :-----                                                                 |
| `"plot"`          | `PLOT`          | Plots a set of X values and Y values linked with lines.                                              | `[[x0,x1,...], [y0,y1,...]]`                                           |
| `"multiplot"`     | `MULTIPLOT`     | Plots several sets of Y values with the same X values on the same figure.                            | `[[x0,x1,...], [[y00,y01,...], [y10,y11,...],...]`                     |
| `"matrix"`        | `MATRIX`        | Plots a `numpy.matrix` object as a matrix                                                            | `numpy.matrix`                                                         |
| `"bar"`           | `BAR`           | Plots a set of data as vertical bars                                                                 | `[v0,v1,v2,...]`                                                       |
| `"multibar"`      | `MULTIBAR`      | Plots several sets of data as vertical bars                                                          | `[[v00,v01,...],[v10,11,...],...]`                                     |
| `"scatter"`       | `SCATTER`       | Plots a set of X values and Y values as points.                                                      | `[[x0,x1,...], [y0,y1,...]]`                                           |
| `"multiscatter"`  | `MULTISCATTER`  | Plots several sets of X and Y values as points on the same figure.                                   | `[[[x00,x01,...],[x10,11,...],...],[[y00,y01,...],[y10,y11,...],...]]` |
| `"histogram"`     | `HISTOGRAM`     | Plots several sets of data as histograms.                                                            | `[[v00,v01,...],[v10,v11,...],...]`                                    |
| `"trace"`         | `TRACE`         | Plots a set of values in the same way as `plot` considered as Y values with their index as X values. | `[v0,v1,v2,...]`                                                       |
| `"multitrace"`    | `MULTITRACE`    | Plots several sets of values as in `trace`. The data sets must be the same length.                   | `[[v00,v01,...],[v10,v11,...],...]`                                    |
| `"stackedbar"`    | `STACKEDBAR`    | Plots several sets of values as stacked bars.                                                        | `[[v00,v01,...],[v10,v11,...],...]`                                    |
| `"pie"`           | `PIE`           | Plots a set of values as a pie.                                                                      | `[v0,v1,v2,...]`                                                       |
| `"matrixscatter"` | `MATRIXSCATTER` | Plots a `numpy.matrix` object as a `multiscatter` figure.                                            | `numpy.matrix`                                                          |
