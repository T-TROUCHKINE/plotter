---
layout: page
title: Legend
permalink: /legend/
---
# Legend
{: .no_toc}
It is possible to add a legend to the figure using the `legend` parameter and by
giving a name for every data set.

- TOC
{:toc}

| Parameter         | Description                                       |
| :-----            | :-----                                            |
| `legend`          | The names to use for the data sets in the legend. |
| `legend_fontsize` | The font size of the legends.                     |
| `legend_location` | The location of the legend over the figure.       |
| `legend_nb_col`   | The number of columns of the legend.              |

### Example
{: .no_toc}
```python
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MULTITRACE,
        "data": [[4,5,8,6,4,5,6,5,2,3,6,4,8,4,5,7,5,4,2,3,1,5,5],
                 [8,4,6,6,9,5,6,5,2,4,5,6,4,8,8,7,9,6,3,1,2,3,6,5,8,4,6,5,5]],
        "legend": ["First set", "Second set"]
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Legend](/img/legend.png)

## Modify legend font size
It is possible to modify the font size of the legend using the `legend_fontsize`
parameter.

### Example
{: .no_toc}
```python
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MULTITRACE,
        "data": [[4,5,8,6,4,5,6,5,2,3,6,4,8,4,5,7,5,4,2,3,1,5,5],
                 [8,4,6,6,9,5,6,5,2,4,5,6,4,8,8,7,9,6,3,1,2,3,6,5,8,4,6,5,5]],
        "legend": ["First set", "Second set"],
        "legend_fontsize": 40
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Legend font size](/img/legend_fontsize.png)

## Specify the legend location
It is possible to set the legend location to a specific value using the
`legend_location` parameter. This parameter can either be a `str` or a `tuple`.

### Example with a string (`str`)
{: .no_toc}
```python
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MULTITRACE,
        "data": [[4,5,8,6,4,5,6,5,2,3,6,4,8,4,5,7,5,4,2,3,1,5,5],
                 [8,4,6,6,9,5,6,5,2,4,5,6,4,8,8,7,9,6,3,1,2,3,6,5,8,4,6,5,5]],
        "legend": ["First set", "Second set"],
        "legend_location": "center left"
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Legend location](/img/legend_location.png)

### Example with a tuple (`tuple`)
{: .no_toc}
```python
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MULTITRACE,
        "data": [[4,5,8,6,4,5,6,5,2,3,6,4,8,4,5,7,5,4,2,3,1,5,5],
                 [8,4,6,6,9,5,6,5,2,4,5,6,4,8,8,7,9,6,3,1,2,3,6,5,8,4,6,5,5]],
        "legend": ["First set", "Second set"],
        "legend_location": (0.5,1.1)
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Legend location using a tuple](/img/legend_location_tuple.png)

## Modify the number of columns of the legend
It is possible to set the number of columns to be used in the legend.

### Example
{: .no_toc}
```python
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MULTITRACE,
        "data": [[4,5,8,6,4,5,6,5,2,3,6,4,8,4,5,7,5,4,2,3,1,5,5],
                 [8,4,6,6,9,4,5,6,4,8,8,7,9,6,3,6,5,8,4,6,5,5],
                 [8,4,6,6,9,5,6,5,2,4,5,6,4,8,8,7,9,6,3,1,2,3,6,5,8,4,6,5,5],
                 [8,4,6,6,8,7,9,6,3,1,2,3,6,5,8,4,6,5,5]],
        "legend": ["First set", "Second set", "Third set", "Fourth set"],
        "legend_nb_col": 3
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Legend font size](/img/legend_nb_col.png)
