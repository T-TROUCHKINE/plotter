---
layout: page
title: Bar
permalink: /bar/
parent: Plot data types
---
# Bar
{: .no_toc}
The `bar` data type able to plot a set of values as bars.

- TOC
{:toc}

## Parameters

| Parameter         | Description                                                     |
| :-----            | :------                                                         |
| `bar_width`       | Set the bar width.                                              |
| `show_data_value` | Display the value of the bars on them.                          |
| `rotate_x_labels` | Rotate the X tick labels of 30° in the trigonometric direction. |

### Example
{: .no_toc}
```python
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.BAR,
        "data": [15,6,5,3,5,8]
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Bar](/img/bar.png)

## Modify the bar width
It is possible to modify the bar width using the `bar_width` parameter.

### Example
{: .no_toc}
```python
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.BAR,
        "data": [15,6,5,3,5,8],
        "bar_width": 0.2
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Bar plot with modified width](/img/bar_width.png)

The total width of a X index is 1. Therefore to avoid the overlapping of the
bars, the `bar_width` parameter must be set to a value lower than 1.
{: .info}

## Show the value of the plotted data
It is possible to show the data value using the `show_data_value` parameter.

### Example
{: .no_toc}
```python
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.BAR,
        "data": [15,6,5,3,5,8],
        "show_data_value": True
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Bar plot with data values](/img/bar_data_val.png)

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
        "type": PlotterType.BAR,
        "data": [15,6,5,3,5,8],
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
![Bar plot with rotated X labels](/img/bar_rotate_labels.png)
