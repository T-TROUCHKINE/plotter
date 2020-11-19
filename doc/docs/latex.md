---
layout: page
title: Latex formatting
permalink: /latex/
---
# Latex formatting
It is possible to format all the text using the Latex formatting by setting the
`latex` argument to `True` in the `Plotter` class.

### Example
```python
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MULTITRACE,
        "data": [[4,5,8,6,4,5,6,5,2,3,6,4,8,4,5,7,5,4,2,3,1,5,5],
                 [8,4,6,6,9,5,6,5,2,4,5,6,4,8,8,7,9,6,3,1,2,3,6,5,8,4,6,5,5]],
        "y_label": "$P^{k \cdot t}$",
        "y_label_fontsize": 30,
        "x_label": "$\sqrt[4]{x^4} = |x|$",
        "x_label_fontsize": 30
    }
]

pl = Plotter(to_plot, latex=True)
pl.show()
```

### Result
![Latex](/img/latex.png)

The `%` corresponds to a comment in Latex and must be escaped using `\%` to
avoid any trouble.
{: .warn}
