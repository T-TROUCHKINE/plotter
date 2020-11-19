---
layout: page
title: Trace
permalink: /trace/
parent: Plot data types
---
# Trace
The `trace` type able to plot a set of values in the same way of the
[`plot`]({{site.baseurl}}/plot/) but with the data index as X values.

### Example
```python
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.TRACE,
        "data": [4,5,8,6,4,5,6,5,2,3,6,4,8,4,5,7,5,4,2,3,1,5,5]
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
![Trace](/img/trace.png)
