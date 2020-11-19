---
layout: page
title: Sub figures
permalink: /subfigures/
---
# Sub figures
It is possible to plot several sub figures by simply adding them to the
`to_plot` table given to the `Plotter` class.

### Example
```python
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MULTITRACE,
        "data": [[4,5,8,6,4,5,6,5,2,3,6,4,8,4,5,7,5,4,2,3,1,5,5],
                 [8,4,6,6,9,5,6,5,2,4,5,6,4,8,8,7,9,6,3,1,2,3,6,5,8,4,6,5,5]],
    },
    {
        "type": PlotterType.MULTIBAR,
        "data": [[4,5,8,6,4,5,6,5,2,3,6,4,8,4,5,7,5,4,2,3,1,5,5],
                 [8,4,6,6,9,5,6,5,2,4,5,6,4,8,8,7,9,6,3,1,2,3,6]],
        "x_ticklabels": [i for i in range(23)]
    },
    {
        "type": PlotterType.SCATTER,
        "data": [[4,5,8,6,4,5,6,5,2,3,6,4,8,4,5,7,5,4,2,3,1,5,5],
                 [8,4,6,6,9,5,6,5,2,4,5,6,4,8,8,7,9,6,3,1,2,3,6]],
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
![Subfigures](/img/subfigures.png)

## Forcing the orientation of the sub figures
It is possible to force the orientation of the sub figures vertically or
horizontally by setting the `force_stack_dir` parameter of the `Plotter` class
to either `"v"` (for vertical stacking) or `"h"`(for horizontal stacking).

### Example
```python
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MULTITRACE,
        "data": [[4,5,8,6,4,5,6,5,2,3,6,4,8,4,5,7,5,4,2,3,1,5,5],
                 [8,4,6,6,9,5,6,5,2,4,5,6,4,8,8,7,9,6,3,1,2,3,6,5,8,4,6,5,5]],
    },
    {
        "type": PlotterType.MULTIBAR,
        "data": [[4,5,8,6,4,5,6,5,2,3,6,4,8,4,5,7,5,4,2,3,1,5,5],
                 [8,4,6,6,9,5,6,5,2,4,5,6,4,8,8,7,9,6,3,1,2,3,6]],
        "x_ticklabels": [i for i in range(23)]
    },
    {
        "type": PlotterType.SCATTER,
        "data": [[4,5,8,6,4,5,6,5,2,3,6,4,8,4,5,7,5,4,2,3,1,5,5],
                 [8,4,6,6,9,5,6,5,2,4,5,6,4,8,8,7,9,6,3,1,2,3,6]],
    }
]

pl = Plotter(to_plot, force_stack_dir="v")
pl.show()
```

### Result
![Subfigures](/img/subfigures_v.png)
