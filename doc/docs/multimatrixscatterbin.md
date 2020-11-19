---
layout: page
title: Multimatrixscatterbin
permalink: /multimatrixscatterbin/
parent: Plot data types
---
# Matrix scatter
{: .no_toc}
The `multimatrixscatterbin` type able to plot multiple
`numpy.matrix` objects as multiple scatters with a binary representation. This
means that every dot on the figure will represent a non zero value of every
matrix.

- TOC
{:toc}

## Parameters

| Parameter        | Description                                       |
| :-------         | :------                                           |
| `image`          | The image to use as a background for the figure.  |
| `revert_X_axis`  | Inverse the X axis.                               |
| `revert_Y_axis`  | Inverse the Y axis.                               |
| `scale_to_image` | Scale the matrix to fill the background image.    |
| `opacity`        | Set the opacity of the dots.                      |

### Example
{: .no_toc}
```python
import numpy as np
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MULTIMATRIXSCATTERBIN,
        "data": [np.matrix([[0,1,0,0],[7,1,2,0],[0,0,2,0],[0,1,0,0]]),
                 np.matrix([[1,0,4,4],[0,0,0,3],[7,0,0,1],[4,0,0,8]])]
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Multimatrixscatterbin](/img/multimatrixscatterbin.png)

## Adding a background image to the figure
It is possible to add a background image to the figure by using the `image`
parameter.

### Example
{: .no_toc}
```python
import numpy as np
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MULTIMATRIXSCATTERBIN,
        "data": [np.matrix([[0,1,0,0],[7,1,2,0],[0,0,2,0],[0,1,0,0]]),
                 np.matrix([[1,0,4,4],[0,0,0,3],[7,0,0,1],[4,0,0,8]])],
        "image": "usa.jpg"
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Multimatrixscatterbin with background image](/img/multimatrixscatterbin_with_img.png)

The used background image is available [here]({{site.baseurl}}/img/usa.jpg).

There are several issues with using the image directly as presented. The
orientation does not match the original orientation of the figure and the size
of the plotted matrix is to low compared with the image size. However, it is
possible to fix both problems.

## Change orientation of the background image
It is possible to inverse the Y axis (or X axis) using the `revert_y_axis` (or
`revert_x_axis`) parameter.

### Example
{: .no_toc}
```python
import numpy as np
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MULTIMATRIXSCATTERBIN,
        "data": [np.matrix([[0,1,0,0],[7,1,2,0],[0,0,2,0],[0,1,0,0]]),
                 np.matrix([[1,0,4,4],[0,0,0,3],[7,0,0,1],[4,0,0,8]])],
        "image": "usa.jpg",
        "revert_y_axis": True
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Multimatrixscatterbin with background image and Y axis reversed](/img/multimatrixscatterbin_with_img_y_reverted.png)

## Scale the matrix to fill the background image
It is possible to upscale the matrix so it fills the used background image using
the `scale_to_image` parameter.

### Example
{: .no_toc}
```python
import numpy as np
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MULTIMATRIXSCATTERBIN,
        "data": [np.matrix([[0,1,0,0],[7,1,2,0],[0,0,2,0],[0,1,0,0]]),
                 np.matrix([[1,0,4,4],[0,0,0,3],[7,0,0,1],[4,0,0,8]])],
        "image": "usa.jpg",
        "revert_y_axis": True,
        "scale_to_image": True
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Multimatrixscatterbin with background image and Y axis reversed and the matrix scaled to the image](/img/multimatrixscatterbin_with_img_y_reverted_scaled.png)

## Modify points opacity
It is possible to modify the opacity of the points using the `opacity` parameter
with a value between 0 and 1.

### Example
{: .no_toc}
```python
import numpy as np
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MULTIMATRIXSCATTERBIN,
        "data": [np.matrix([[0,1,0,0],[7,1,2,0],[0,0,2,0],[0,1,0,0]]),
                 np.matrix([[1,0,4,4],[0,0,0,3],[7,0,0,1],[4,0,0,8]])],
        "image": "usa.jpg",
        "revert_y_axis": True,
        "scale_to_image": True,
        "opacity": 0.5
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Multimatrixscatterbin with background image and Y axis reversed and the matrix scaled to the image and low opacity points](/img/multimatrixscatterbin_with_img_y_reverted_scaled_opacity.png)
