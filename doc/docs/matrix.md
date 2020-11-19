---
layout: page
title: Matrix
permalink: /matrix/
parent: Plot data types
---
# Matrix
{: .no_toc}
The `matrix` type able to plot a `numpy.matrix` object with its corresponding
color-bar.

1. TOC
{:toc}

## Parameters

| Parameter        | Description                                       |
| :-------         | :------                                           |
| `colorbar_label` | The label to use for the color bar.               |
| `no_colorbar`    | If set to `True`, the color bar is not displayed. |

### Example
{: .no_toc}
```python
import numpy as np
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MATRIX,
        "data": np.matrix([[0,1,2,3,4,5],[15,6,5,3,5,8],[8,6,9,12,3,5],[4,5,7,7,5,3]]),
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Matrix](/img/matrix.png)

## Adding a label to the color bar
It is possible to add a label to the color bar using the `colorbar_label`
parameter.

### Example
{: .no_toc}
```python
import numpy as np
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MATRIX,
        "data": np.matrix([[0,1,2,3,4,5],[15,6,5,3,5,8],[8,6,9,12,3,5],[4,5,7,7,5,3]]),
        "colorbar_label": "Awesome label"
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Matrix with colorbar label](/img/matrix_cb_label.png)

## Remove the color bar
It is possible to no print the color bar by using the `no_colorbar` parameter.
The presence of the parameter is enough to remove the color bar, its value has
no importance at all.

### Example
{: .no_toc}
```python
import numpy as np
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MATRIX,
        "data": np.matrix([[0,1,2,3,4,5],[15,6,5,3,5,8],[8,6,9,12,3,5],[4,5,7,7,5,3]]),
        "no_colorbar": True
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Matrix without colorbar](/img/matrix_no_cb.png)
