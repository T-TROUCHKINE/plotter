# Plotter Documentation
## Plotter class
This class helps in managing the plotting of figures.

__Methods__

- Constructor: constructor of the class

  _Arguments_
  - `to_plot` (mandatory): reference containing all the figures to plot or the
    number of figure to plot
  - `figsuptitle`: title of the complete figure (default=`None`)
  - `figsize`: size of the window (default=`(20,20)`)
  - `tikz_file`: name of the file storing the Latex description of the figure
    (default=`""`)
  
- `set_to_plot(to_plot)`: set the figure to plot, the `to_plot` argument must be
  a list of dictionaries, each diction nary describing a figure.
- `set_show_title(val)`: set the `show_titles` flag to `val`, when set to
  `False` the titles are not displayed on the figure. Useful for GTK integration
  for example.
- `export_tikz(filename)`: export the Latex equivalent of the figure in the file
  `filename`.
- `show(blocking)`: display the figure, the `blocking` argument is optional
  (default=`True`). When `blocking` is set to `False`, then putting this
  function in a loop will do a real time plotting. Therefore, the new figure to
  plot must be set via the `set_to_plot` method.
- `set_axes_aspect()`: display the subfigure to occupy the whole available
  space. Useful when a figure switch in different data types.
  
## Figure description
A figure is a list of dictionaries. Each dictionary is the description of a
subfigure. The description is based on a `"attribute": value` organization.

### Attributes of the subfigures

- title (String): title of the subfigure, is mandatory but can be empty.
- data: the data to plot
- type (String): way the data must be plotted. The current values available are:
  - plot: plot the data as a (x,y) function the data must be a list of two lists
    representing the y-axis and the x-axis.
  - matrix: plot the data as matrix, the data must be a 2-entry list.
  - bar: plot the data as bars, the data must be a 1-entry list.
  - scatter: plot the data as a scatter, the data must be a 2-entry list.
  - histogram: plot the data as a frequency histogram, the data must be a
    1-entry list but several lists can be given and will be treated as different
    data sets.
  - trace: plot the data as a trace, the data must be a 1-entry list
  - multitrace: plot the data as trace, the data must be a list of lists, every
    list will be plotted as different data sets, note that `{"type": "trace",
    "data": trace}` is equivalent to `{"type": "multitrace", "data": [trace]}`.
- x_label (optional String): the label describing the x-axis.
- y_label (optional String): the label describing the y-axis.
- x_ticklabels (optional String list): the labels describing the values of the
  all the ticks on the x-axis of the figure, useful for bar type plot
- x\_ticklabels\_fontsize (optional Integer): set the font size of the ticks on
  the x-axis
- y\_ticklabels\_fontsize (optional Integer): set the font size of the ticks on
  the y-axis
- show_grid (optional Boolean): show or not a grid
- rotate\_x\_label (optional Boolean): rotate the labels used for the ticks to
  avoid superposition.
- show\_data\_value (specific to bar type Boolean): show the values on the bars.
- data\_value\_color (specific to bar type String): set the color of the values
  displayed on the bars.
- data\_value\_fontsize (specific to bar type Integer): set the fontsize of the
  values displayed on the bars.
- bar_width (specific to bar type Float): set the width of the displayed bars
