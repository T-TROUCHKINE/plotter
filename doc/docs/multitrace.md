---
layout: page
title: Multitrace
permalink: /multitrace/
parent: Plot data types
---
# Multitrace
The `multitrace` type able to plot a set of values in the same way of the
[`multiplot`]({{site.baseurl}}/multiplot/) type but with the data index as X
values.

### Example
```python
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MULTITRACE,
        "data": [[4,5,8,6,4,5,6,5,2,3,6,4,8,4,5,7,5,4,2,3,1,5,5],
                 [8,4,6,6,9,5,6,5,2,4,5,6,4,8,8,7,9,6,3,1,2,3,6,5,8,4,6,5,5]]
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
![Multitrace](/img/multitrace.png)
