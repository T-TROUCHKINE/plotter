---
layout: page
title: Matrixscatter
permalink: /matrixscatter/
parent: Plot data types
---
# Matrix scatter
{: .no_toc}
The `matrixscatter` type able to plot a `numpy.matrix` object as multiple
scatters with its corresponding color bar.

- TOC
{:toc}

## Parameters

| Parameter        | Description                                       |
| :-------         | :------                                           |
| `colorbar_label` | The label to use for the color bar.               |
| `no_colorbar`    | If set to `True`, the color bar is not displayed. |
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
        "type": PlotterType.MATRIXSCATTER,
        "data": np.matrix([[0,1,2,3,4,5],[15,6,5,3,5,8],[8,6,9,12,3,5],[4,5,7,7,5,3]]),
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Matrixscatter](/img/matrixscatter.png)

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
        "type": PlotterType.MATRIXSCATTER,
        "data": np.matrix([[0,1,2,3,4,5],[15,6,5,3,5,8],[8,6,9,12,3,5],[4,5,7,7,5,3]]),
        "colorbar_label": "Awesome label"
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Matrixscatter with colorbar label](/img/matrixscatter_cb_label.png)

## Remove the colorbar
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
        "type": PlotterType.MATRIXSCATTER,
        "data": np.matrix([[0,1,2,3,4,5],[15,6,5,3,5,8],[8,6,9,12,3,5],[4,5,7,7,5,3]]),
        "no_colorbar": True
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Matrixscatter without colorbar](/img/matrixscatter_no_cb.png)

## Adding a background image to the figure
Using the `matrixscatter` type, it is possible to add a background image to the
figure by using the `image` parameter.

### Example
{: .no_toc}
```python
import numpy as np
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MATRIXSCATTER,
        "data": np.matrix([[0,1,2,3,4,5],[15,6,5,3,5,8],[8,6,9,12,3,5],[4,5,7,7,5,3]]),
        "image": "usa.jpg"
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Matrixscatter with background image](/img/matrixscatter_with_img.png)

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
        "type": PlotterType.MATRIXSCATTER,
        "data": np.matrix([[0,1,2,3,4,5],[15,6,5,3,5,8],[8,6,9,12,3,5],[4,5,7,7,5,3]]),
        "image": "usa.jpg",
        "revert_y_axis": True
    }
]

pl = Plotter(to_plot)
pl.show()
```

### Result
{: .no_toc}
![Matrixscatter with background image and Y axis reversed](/img/matrixscatter_with_img_y_reverted.png)

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
        "type": PlotterType.MATRIXSCATTER,
        "data": np.matrix([[0,1,2,3,4,5],[15,6,5,3,5,8],[8,6,9,12,3,5],[4,5,7,7,5,3]]),
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
![Matrixscatter with background image and Y axis reversed and the matrix scaled to the image](/img/matrixscatter_with_img_y_reverted_scaled.png)

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
        "type": PlotterType.MATRIXSCATTER,
        "data": np.matrix([[0,1,2,3,4,5],[15,6,5,3,5,8],[8,6,9,12,3,5],[4,5,7,7,5,3]]),
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
![Matrixscatter with background image and Y axis reversed and the matrix scaled to the image and low opacity points](/img/matrixscatter_with_img_y_reverted_scaled_opacity.png)
