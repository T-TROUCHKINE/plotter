---
layout: page
title: Text
permalink: /text/
---
# Text
It is possible to add text somewhere on the figure using the `text` parameter.

| Parameter | Description                                                                                    |
| :----     | :----                                                                                          |
| `text`    | A table containing the triplets (X position, Y position, "Text") describing the text to write. |

### Example
```python
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MULTITRACE,
        "data": [[4,5,8,6,4,5,6,5,2,3,6,4,8,4,5,7,5,4,2,3,1,5,5],
                 [8,4,6,6,9,5,6,5,2,4,5,6,4,8,8,7,9,6,3,1,2,3,6,5,8,4,6,5,5]],
        "text": [(5,7,"Some funny text")]
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
![Text](/img/text.png)
