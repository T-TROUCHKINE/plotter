---
layout: page
title: Getting started
permalink: /start/
nav_order: 1
---

# Getting started

## Installation

### Linux packages
- **tk**:

| Distribution   | Command          |
| :------------- | :--------        |
| ArchLinux      | `pacman -S tk`   |
| Debian         | `apt install tk` |

### Python libraries

| Library     | Command                 |
| :---        | :--                     |
| matplotlib  | `pip install matplotlib` |
| numpy       | `pip install numpy`     |
| tikzplotlib | `pip install tikzplotlib` |

### GTK3
For installing GTK3 modules see [PyGObject documentation](https://pygobject.readthedocs.io/en/latest/getting_started.html).

### Plotter
`pip install plotter`

## First plot
### Code
```python
import numpy as np
from plotter import Plotter

x = np.linspace(-np.pi, np.pi, 201)

to_plot = [{
    "title": "Example",
    "type": "plot",
    "data": [x, np.sin(x)]
}]

pl = Plotter(to_plot)
pl.show()
```
### Result
![First plot result](/img/ex1.png)
