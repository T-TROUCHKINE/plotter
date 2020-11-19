---
layout: page
title: Figure title
permalink: /title/
---
# Figure title
It is possible to add a title to the figure and customize it using the `title`
and `title_fontsize` parameters.

| Parameter        | Description              |
| :-----           | :------                  |
| `title`          | The title of the figure. |
| `title_fontsize` | The title font size.     |

### Example
```python
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MULTITRACE,
        "data": [[4,5,8,6,4,5,6,5,2,3,6,4,8,4,5,7,5,4,2,3,1,5,5],
                 [8,4,6,6,9,5,6,5,2,4,5,6,4,8,8,7,9,6,3,1,2,3,6,5,8,4,6,5,5]],
        "title": "Awesome title !",
        "title_fontsize": 40
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
![Title](/img/title.png)
