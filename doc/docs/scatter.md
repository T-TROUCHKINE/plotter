---
layout: page
title: Scatter
permalink: /scatter/
parent: Plot data types
---
# Scatter
{: .no_toc}
The `scatter` plot able to plot a set of X and Y values as points.

- TOC
{:toc}

## Parameters

| Parameter       | Description                                      |
| :-------        | :------                                          |
| `image`         | The image to use as a background for the figure. |
| `revert_X_axis` | Inverse the X axis.                              |
| `revert_Y_axis` | Inverse the Y axis.                              |

### Example
{: .no_toc}
```python
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.SCATTER,
        "data": [[15,6,5,3,5,8],[5,6,8,9,6,3]]
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Scatter](/img/scatter.png)

## Adding a background image to the figure
Using the `scatter` type, it is possible to add a background image to the figure
by using the `image` parameter.

### Example
{: .no_toc}
```python
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.SCATTER,
        "data": [[15,6,5,3,5,8],[5,6,8,9,6,3]],
        "image": "usa.jpg"
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Matrixscatter with background image](/img/scatter_with_img.png)

The used background image is available [here]({{site.baseurl}}/img/usa.jpg).

There are several issues with using the image directly as presented. The
orientation does not match the original orientation of the figure.

## Change orientation of the background image
It is possible to inverse the Y axis (or X axis) using the `revert_y_axis` (or
`revert_x_axis`) parameter.

### Example
{: .no_toc}
```python
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.SCATTER,
        "data": [[15,6,5,3,5,8],[5,6,8,9,6,3]],
        "image": "usa.jpg",
        "revert_y_axis": True
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Scatter with background image and Y axis reversed](/img/scatter_with_img_y_reverted.png)
