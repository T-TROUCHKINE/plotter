---
layout: page
title: Grid
permalink: /grid/
---
# Grid
It is possible to display a grid on the figure using various parameters.

| Parameter    | Description                                |
| :--------    | :-------                                   |
| `show_grid`  | Display a grid on the figure.              |
| `show_xgrid` | Display only vertical lines of the grid.   |
| `show_ygrid` | Display only horizontal lines of the grid. |

### Example
```python
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MULTITRACE,
        "data": [[4,5,8,6,4,5,6,5,2,3,6,4,8,4,5,7,5,4,2,3,1,5,5],
                 [8,4,6,6,9,5,6,5,2,4,5,6,4,8,8,7,9,6,3,1,2,3,6,5,8,4,6,5,5]],
        "show_grid": True
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
![Grid](/img/grid.png)
