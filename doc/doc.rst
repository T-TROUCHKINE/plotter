Help on module plotter.plotter in plotter:

NAME
    plotter.plotter

CLASSES
    builtins.object
        Plotter
    enum.Enum(builtins.object)
        PlotterType
    
    class Plotter(builtins.object)
     |  Plotter(to_plot, figsuptitle=None, figsize=(20, 20), tikz_file='')
     |  
     |  Class used for plotting data.
     |  
     |  This class must take as argument a dictionary containing the description
     |  and the data of the figures you want to plot.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, to_plot, figsuptitle=None, figsize=(20, 20), tikz_file='')
     |      Constructor function of the Class Plotter.
     |      
     |      Initialize the Plotter class with figures to plot or the number of figures to plot.
     |      
     |      Arguments:
     |      
     |      to_plot - a dictionnary containing the figures to plot or an integer
     |      containing the number of figures to plot.
     |      
     |      figsuptitle - a string containing the title of the whole plot (default:
     |      None).
     |      
     |      figsize - a tuple containing the size of the window containing the
     |      figures (default: (20,20)).
     |      
     |      tikz_file - a string containing the path to the file where save the
     |      Tikz description of the figure (default: "").
     |  
     |  add_legend(self, to_plot, axe)
     |      Add a legend to the plot.
     |      
     |      Arguments:
     |      
     |      to_plot - the dictionnary to parse for getting legend information.
     |      
     |      axe - the subfigure where to add the legend.
     |      
     |      TODO: Make private.
     |  
     |  clean_axes(self)
     |      Clean axes. Usefull for dynamic plot.
     |      
     |      TODO: Make private.
     |  
     |  clean_plot(self)
     |      Clean the figures before plotting. Usefull for dynamic plot.
     |      
     |      TODO: Make private.
     |  
     |  export_tikz(self, filename='tikz_fig.tex')
     |      Export the figure to a tikz file. This method cannot be called after the
     |      show() method otherwise the result file will not containing the figure.
     |      
     |      Arguments:
     |      
     |      filename - the path to the file where to store the tikz description of
     |      the figure (default: "tikz_fig.tex").
     |  
     |  get_bar_width(self, to_plot)
     |      Return the bar width parameter parsed from the to_plot dictionnary.
     |      
     |      Arguments:
     |      
     |      to_plot - the dictionnary to parse the bar width from.
     |      
     |      TODO: Make private.
     |  
     |  get_bounds_and_norm(self, matrix)
     |      Return the needed parameters for a clean colorbar for a Matrix plot.
     |      
     |      Arguments:
     |      
     |      matrix - the matrix to build a colorbar to.
     |      
     |      TODO: Make private.
     |  
     |  get_data_value_caract(self, to_plot)
     |      Return the parameters for the data value to show in bar plot.
     |      
     |      Arguments:
     |      
     |      to_plot - the dictionnary to parse for getting the data value parameters.
     |      
     |      TODO: Make private.
     |  
     |  get_fig(self)
     |      Return the Matplotlib figure object of the plot.
     |  
     |  get_figsize(self)
     |      Return the size of the window plotting the figures.
     |  
     |  get_figsuptitle(self)
     |      Return the main title of the plot.
     |  
     |  get_label_fontsize(self, to_plot, coord)
     |      Return the label font size parsed from the to_plot dictionnary.
     |      
     |      Arguments:
     |      
     |      to_plot - the dictionnary to parse for getting the label font size.
     |      
     |      coord - the axis of the label to get the font size.
     |      
     |      TODO: Make private.
     |  
     |  get_xlabel_fontsize(self, to_plot)
     |      Return the label font size of the label on x axis parsed from the to_plot
     |      dictionnary.
     |      
     |      Arguments:
     |      
     |      to_plot - the dictionnary to parse for getting the label font size.
     |      
     |      TODO: Make private.
     |  
     |  get_ylabel_fontsize(self, to_plot)
     |      Return the label font size of the label on y axis parsed from the to_plot
     |      dictionnary.
     |      
     |      Arguments:
     |      
     |      to_plot - the dictionnary to parse for getting the label font size.
     |      
     |      TODO: Make private.
     |  
     |  init_fig_subplot(self)
     |      Initialize the figure and axes for the plot plot.
     |      
     |      TODO: Make private.
     |  
     |  init_plot(self)
     |      Initialize the plot.
     |      
     |      TODO: Make private.
     |  
     |  plot_bar(self, to_plot, axe)
     |      Plot bars from one data set.
     |      
     |      Arguments:
     |      
     |      to_plot - the dictionnary containing the information for the plot.
     |      
     |      axe - the subfigure where to plot the bars.
     |      
     |      TODO: Make private.
     |  
     |  plot_data(self)
     |      Plot the data from the to_plot parameter.
     |      
     |      TODO: Make private.
     |  
     |  plot_matrix(self, to_plot, axe)
     |      Plot a matrix.
     |      
     |      Arguments:
     |      
     |      to_plot - the dictionnary containing the information for plotting the matrix.
     |      
     |      axe - the subfigure where to plot the matrix.
     |      
     |      TODO: Make private.
     |  
     |  plot_multibar(self, to_plot, axe)
     |      Plot bars from multiple data set.
     |      
     |      Arguments:
     |      
     |      to_plot - the dictionnary containing the information for the plot.
     |      
     |      axe - the subfigure where to plot the bars.
     |      
     |      TODO: Make private.
     |  
     |  remove_colorbars(self)
     |      Remove the colorbars in the figures. Usefull for dynamic plot as colorbars
     |      are stacking while repeating the plot.
     |      
     |      TODO: Make private.
     |  
     |  set_axes_aspect(self)
     |      Adapt the aspect of the subfigures. Usefull when a subfigure type of plot is
     |      changing, like in the Gtk3 example for instance.
     |  
     |  set_colormap(self, cmap)
     |      Set the colormap. Mainly used in matrix figures.
     |      
     |      Arguments:
     |      
     |      cmap - the cmap object from Matplotlib to use as a colormap.
     |  
     |  set_figsize(self, figsize)
     |      Set the size of the window plotting the figure.
     |      
     |      Arguments:
     |      
     |      figsize - a tuple describing the size of window to use.
     |  
     |  set_figsuptitle(self, suptitle)
     |      Set the main title of the plot.
     |      
     |      Arguments:
     |      
     |      suptitle - the string containing the main title to use for the plot.
     |  
     |  set_grid(self)
     |      Set the grid in the figures.
     |      
     |      TODO: Make private.
     |  
     |  set_informations(self)
     |      Set information on the plots.
     |      
     |      TODO: Make private.
     |  
     |  set_labels(self)
     |      Set the labels in the figures.
     |      
     |      TODO: Make private.
     |  
     |  set_show_titles(self, val)
     |      Set the show_titles parameter. If set to True the figures will all have a
     |      title above their plot.
     |      
     |      Arguments:
     |      
     |      val - the boolean value to set show_titles to.
     |      
     |      TODO: use the setter/getter function of Python
     |  
     |  set_ticklabels(self)
     |      Set the labels for the thicks in the figures.
     |      
     |      TODO: Make private.
     |  
     |  set_titles(self)
     |      Set the title of the figures from the to_plot object.
     |      
     |      TODO: Make private.
     |  
     |  set_to_plot(self, to_plot)
     |      Set the figures plot.
     |      
     |      Arguments:
     |      
     |      to_plot - a dictionnary containing the description of the figures to
     |      plot.
     |  
     |  show(self, blocking=True)
     |      Show the figure.
     |      
     |      Arguments:
     |      
     |      blocking - if set to True, the program will stall on this function
     |      while the window is remained opened (default: True).
     |  
     |  show_text_value(self, to_plot, axe)
     |      Add the values of bars as text.
     |      
     |      Arguments:
     |      
     |      to_plot - the dictionnary containing the information about how to display the values.
     |      
     |      axe - the subfigure where to show the values of data.
     |      
     |      TODO: Make private.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class PlotterType(enum.Enum)
     |  PlotterType(value, names=None, *, module=None, qualname=None, type=None, start=1)
     |  
     |  Class containing all possible ways to plot data using plotter.
     |  
     |  Use these values for the "type" paramater in the description of your
     |  figure.
     |  
     |  Method resolution order:
     |      PlotterType
     |      enum.Enum
     |      builtins.object
     |  
     |  Data and other attributes defined here:
     |  
     |  BAR = <PlotterType.BAR: 7>
     |  
     |  HISTOGRAM = <PlotterType.HISTOGRAM: 3>
     |  
     |  MATRIX = <PlotterType.MATRIX: 1>
     |  
     |  MULTIBAR = <PlotterType.MULTIBAR: 8>
     |  
     |  MULTITRACE = <PlotterType.MULTITRACE: 6>
     |  
     |  PLOT = <PlotterType.PLOT: 5>
     |  
     |  SCATTER = <PlotterType.SCATTER: 2>
     |  
     |  TRACE = <PlotterType.TRACE: 4>
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from enum.Enum:
     |  
     |  name
     |      The name of the Enum member.
     |  
     |  value
     |      The value of the Enum member.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from enum.EnumMeta:
     |  
     |  __members__
     |      Returns a mapping of member name->value.
     |      
     |      This mapping lists all enum members, including aliases. Note that this
     |      is a read-only view of the internal mapping.

FILE
    /home/kerzas/Documents/Dev/Python/plotter/plotter/plotter.py


