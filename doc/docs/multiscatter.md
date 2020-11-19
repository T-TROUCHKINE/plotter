---
layout: page
title: Multiscatter
permalink: /multiscatter/
parent: Plot data types
---
# Multiscatter
{: .no_toc}
The `multiscatter` plot able to plot several sets of X and Y values as points.

- TOC
{:toc}

## Parameters

| Parameter       | Description                                      |
| :-------        | :------                                          |
| `image`         | The image to use as a background for the figure. |
| `revert_X_axis` | Inverse the X axis.                              |
| `revert_Y_axis` | Inverse the Y axis.                              |
| `marker_color`  | Set the colors of the data sets.                 |

### Example
{: .no_toc}
```python
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MULTISCATTER,
        "data": [[[1500,654,541,312,511,884],[506,65,847,911,64,353]],
                 [[456,123,684,475,1245,552,124],[458,44,667,542,986,45,788]]]
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Multiscatter](/img/multiscatter.png)

## Adding a background image to the figure
Using the `multiscatter` type, it is possible to add a background image to the
figure by using the `image` parameter.

### Example
{: .no_toc}
```python
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MULTISCATTER,
        "data": [[[1500,654,541,312,511,884],[506,65,847,911,64,353]],
                 [[456,123,684,475,1245,552,124],[458,44,667,542,986,45,788]]]
        "image": "usa.jpg"
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Multiscatter with background image](/img/multiscatter_with_img.png)

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
        "type": PlotterType.MULTISCATTER,
        "data": [[[1500,654,541,312,511,884],[506,65,847,911,64,353]],
                 [[456,123,684,475,1245,552,124],[458,44,667,542,986,45,788]]]
        "image": "usa.jpg",
        "revert_y_axis": True
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Multiscatter with background image and Y axis reversed](/img/multiscatter_with_img_y_reverted.png)

## Custom the color for the scatter points
It is possible to use a custom color for the scatter points using the
`marker_color` parameter and by giving the hexadecimal string of the desired
color.

### Example
{: .no_toc}
```python
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MULTISCATTER,
        "data": [[[1500,654,541,312,511,884],[506,65,847,911,64,353]],
                 [[456,123,684,475,1245,552,124],[458,44,667,542,986,45,788]]],
        "marker_color": ["#70161e", "#1c3144"]
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Multiscatter with custom colors](/img/multiscatter_color.png)
