---
layout: page
title: Ticklabels
permalink: /ticklabels/
---
# Tick labels
The tick labels can be fully customized using various parameters.

| Parameter               | Description                                                                      |
| :-----                  | :-----                                                                           |
| `x_ticklabels`          | The table containing the strings corresponding to the tick labels of the X axis. |
| `y_ticklabels`          | The table containing the strings corresponding to the tick labels of the X axis. |
| `x_ticklabels_position` | The table of the coordinates where to put the tick labels of the X axis.         |
| `y_ticklabels_position` | The table of the coordinates where to put the tick labels of the Y axis.         |
| `x_ticklabels_fontsize` | The font size of the tick labels of the X axis.                                  |
| `y_ticklabels_fontsize` | The font size of the tick labels of the Y axis.                                  |
| `ticklabels_fontsize`   | The font size of all the tick labels.                                            |

### Example
```python
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MULTITRACE,
        "data": [[4,5,8,6,4,5,6,5,2,3,6,4,8,4,5,7,5,4,2,3,1,5,5],
                 [8,4,6,6,9,5,6,5,2,4,5,6,4,8,8,7,9,6,3,1,2,3,6,5,8,4,6,5,5]],
        "x_ticklabels": ["Some", "custom", "tick", "labels"],
        "x_ticklabels_position": [3,8,13,20],
        "x_ticklabels_fontsize": 28,
        "y_ticklabels": ["Some", "others"],
        "y_ticklabels_position": [2,8],
        "y_ticklabels_fontsize": 16
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
![Ticklabels](/img/ticklabels.png)
