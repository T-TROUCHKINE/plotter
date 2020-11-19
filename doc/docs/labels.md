---
layout: page
title: Labels
permalink: /labels/
---
# Labels
The labels can be customized using various parameters.

| Parameter          | Description                        |
| :-----             | :-----                             |
| `x_label`          | The label of the X axis.           |
| `y_label`          | The label of the Y axis.           |
| `x_label_fontsize` | The font size of the X axis label. |
| `y_label_fontsize` | The font size of the Y axis label. |

### Example
```python
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MULTITRACE,
        "data": [[4,5,8,6,4,5,6,5,2,3,6,4,8,4,5,7,5,4,2,3,1,5,5],
                 [8,4,6,6,9,5,6,5,2,4,5,6,4,8,8,7,9,6,3,1,2,3,6,5,8,4,6,5,5]],
        "x_label": "My X axis",
        "x_label_fontsize": 20,
        "y_label": "The POWER",
        "y_label_fontsize": 28
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
![Labels](/img/labels.png)
