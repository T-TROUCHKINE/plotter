---
layout: page
title: Plot
permalink: /plot/
parent: Plot data types
---
# Plot
{: .no_toc}
The `plot` type is the most basic type. It able to plot a set of X and Y values.
The plotted points are linked using lines.

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
        "type": PlotterType.PLOT,
        "data": [[0,1,2,3,4,5], [15,6,5,3,5,8]]
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Minimal parameters plot](/img/ex2.png)

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
        "type": PlotterType.PLOT,
        "data": [[0,1,2,3,4,5], [15,6,5,3,5,8]],
        "marker": "-o"
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Plot with markers](/img/marked_plot.png)

## Multiple plots on the same figure
For plotting several plots on the same figure see [multiplot]({{site.baseurl}}/multiplot).
