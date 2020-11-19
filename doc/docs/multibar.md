---
layout: page
title: Multibar
permalink: /multibar/
parent: Plot data types
---
# Multibar
{: .no_toc}
The `multibar` data type able to plot several set of values as bars.

- TOC
{:toc}

## Parameters

| Parameter         | Description                                                     |
| :-------          | :------                                                         |
| `bar_width`       | Set the bar width.                                              |
| `rotate_X_labels` | Rotate the X tick labels of 30° in the trigonometric direction. |
| `colors`          | Set the colors of the data sets.                                |

### Example
{: .no_toc}
```python
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MULTIBAR,
        "data": [[15,6,5,3,5,8],[5,6,8,9,6,3]],
        "x_ticklabels": ["One", "Two", "Three", "Four", "Five", "Six"]
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Multibar](/img/multibar.png)

While using the `multibar` type, it is mandatory to give the `x_ticklabels` parameter as well.
{: .warn}

## Modify the bar width
It is possible to modify the bar width using the `bar_width` parameter.

### Example
{: .no_toc}
```python
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MULTIBAR,
        "data": [[15,6,5,3,5,8],[5,6,8,9,6,3]],
        "x_ticklabels": ["One", "Two", "Three", "Four", "Five", "Six"],
        "bar_width": 0.49
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Multibar plot with modified width](/img/multibar_width.png)

The total width of all bar at a specific index is 1. So, to avoid any overlap,
the width must be lower than 1 divided by the number of data sets. 
{: .info}

## Rotate the X axis labels
In the case the X axis labels are very large, it is interesting to rotate them
to make the figure more readable. This can be achieved using the
`rotate_x_labels` parameter.

### Example
{: .no_toc}
```python
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MULTIBAR,
        "data": [[15,6,5,3,5,8],[5,6,8,9,6,3]],
        "x_ticklabels": ["very_mega_large_label_one",
                         "very_mega_large_label_two",
                         "very_mega_large_label_three",
                         "very_mega_large_label_four",
                         "very_mega_large_label_five",
                         "very_mega_large_label_six"],
        "rotate_x_labels": True
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Multibar plot with rotated X labels](/img/multibar_rotate_labels.png)

## Modify the color of the bars
It is possible to modify the color of the bars using the `colors` parameter with
the colors to use described as their hexadecimal value.

### Example
{: .no_toc}
```python
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MULTIBAR,
        "data": [[15,6,5,3,5,8],[5,6,8,9,6,3]],
        "x_ticklabels": ["One", "Two", "Three", "Four", "Five", "Six"],
        "colors": ["#70161e", "#1c3144"]
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Multibar plot with custom colors](/img/multibar_color.png)

This `multibar` plot is the only type supporting the color customization.
{: .info}
