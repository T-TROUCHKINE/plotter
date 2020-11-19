---
layout: page
title: Figure dictionary
permalink: /dict/
nav_order: 3
---
# Figure dictionary
In Plotter, a figure is described using a dictionary. The dictionary contains every information one wants on its figures. The dictionary's key represent the parameter and its value the corresponding value in the figure.

## Mandatory parameters
A figure dictionary has only two mandatory parameters.

| Parameter | Type                            | Description                                            |
| :------   | :----                           | :----                                                  |
| `type`    | `str` or `PlotterType`          | Define the way the data will be plotted in the figure. |
| `data`    | Depends on the `type` parameter | The data to plot                                       |

### Example
```python
from plotter import Plotter

to_plot = [
    {
        "type": "plot",
        "data": [[0,1,2,3,4,5], [15,6,5,3,5,8]]
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
![Minimal parameters plot](/img/ex2.png)

Creating such dictionary is the start, but `Plotter` supports more ways to plot your data.

<span class="fs-4">
[Plot data types >>]({{site.baseurl}}/types/){: .btn}
</span>
