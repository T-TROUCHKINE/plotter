---
layout: page
title: Multiplot
permalink: /multiplot/
parent: Plot data types
---
# Multiplot
{: .no_toc}
The `multiplot` type is the plot several Y set values with the same X values in
the same way as the `plot` type but on the same figure.

- TOC
{:toc}

## Parameters

| Parameter | Description                                    |
| :-----    | :------                                        |
| `marker`  | The marker to display at the data coordinates. |

### Example
{: .no_toc}
```python
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MULTIPLOT,
        "data": [[0,1,2,3,4,5], [[15,6,5,3,5,8],[8,6,9,12,3,5]]]
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Multiplot](/img/multiplot.png)

## Markers
It is possible to add markers to the plot to highlight the points using the
`marker` parameter. The possible values for the markers are the one supported by
Matplotlib ([see doc](https://matplotlib.org/3.3.1/api/markers_api.html)).

### Example
{: .no_toc}
```python
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MULTIPLOT,
        "data": [[0,1,2,3,4,5], [[15,6,5,3,5,8],[8,6,9,12,3,5]]],
        "marker": "-o"
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Multiplot with markers](/img/marked_multiplot.png)
