import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from tikzplotlib import save as tikz_save
from enum import Enum

types_str = ["matrix", "scatter", "histogram", "trace", "plot", "multitrace", "bar", "multibar", "pie", "multiscatter", "matrixscatter"]

class PlotterType(Enum):
    """Class containing all possible ways to plot data using plotter. Use these values for the "type" paramater in the description of your figure.

    """
    MATRIX = 1
    SCATTER = 2
    HISTOGRAM = 3
    TRACE = 4
    PLOT = 5
    MULTITRACE = 6
    BAR = 7
    MULTIBAR = 8
    PIE = 9
    MULTISCATTER = 10
    MATRIXSCATTER = 11

class Plotter:
    """Class used for plotting data. This class must take as argument a dictionary containing the description and the data of the figures you want to plot.

    """
    def __init__(self, to_plot, figsuptitle=None, figsize=(20, 20),
                 tikz_file="", cmap=plt.cm.jet, latex=False):
        """Constructor function of the Class Plotter. Initialize the Plotter class with figures to plot or the number of figures to plot.

        :param list/int to_plot: a list of dictionaries containing the figures to plot or an integer containing the number of figures to plot.
        :param str figsuptitle: the title of the whole plot (default: None).
        :param tuple figsize: the size of the window containing the figures (default: (20,20)).
        :param str tikz_file: the path to the file where save the Tikz description of the figure (default: "").
        :param ColorMap cmap: the ColorMap to use for the plot.
        :param bool latex: a flag for choosing to have the Latex font used on the plot or not.

        """
        if latex:
            plt.rc("text", usetex=True)
            plt.rc("font", family="serif")

        self.figsize = figsize
        """The size of the window containing the figures."""
        self.figsuptitle = figsuptitle
        """The title of the whole plot."""
        self.fig = None
        """The Figure object which contains the plots"""

        self.nb_to_plot = 0
        """The number of subfigures in the plot."""
        self.to_plot = None
        """The list of dictionaries describing the figures to plot."""

        if isinstance(to_plot, int):
            self.nb_to_plot = to_plot
        elif isinstance(to_plot, list):
            self.to_plot = to_plot
            self.nb_to_plot = len(self.to_plot)

        self.axes = None
        """The Axes objects of each subfigures."""
        self.colorbars = None
        """The Coloarbar objects of the subfigures."""
        self.cmap = cmap
        """The ColorMap used for the plot."""
        self.show_titles = True
        """A flag that set if the titles of the subfigures have to be visible or not."""

        self.tikz_export = False
        """A flag that set if the plot must be exported in a Tikz file."""
        self.tikz_file = None
        """"The string containing the path to the file of the Tikz file."""

        if len(tikz_file) > 0:
            self.tikz_file = tikz_file
            self.tikz_export = True

        self.init_plot()

    def set_show_titles(self, val):
        """Set the show_titles parameter. If set to True the figures will all have a title above their plot.

        :param bool val: the value to set the show_titles flag to.

        :TODO: remove the method and use the direct reference.

        """
        self.show_titles = val

    def get_fig(self):
        """:returns: the Matplotlib figure object of the plot.

        :TODO: remove the method and use the direct reference.

        """
        return self.fig

    def set_colormap(self, cmap):
        """Change the colormap used for the plot.

        :param Colormap cmap: the Colormap object from Matplotlib to use as a colormap.

        :TODO: remove the method and use the direct reference.

        """
        self.cmap = cmap

    def get_figsize(self):
        """:returns: the size of the window plotting the figures.

        :TODO: remove the method and use the direct reference.

        """
        return self.figsize

    def set_figsize(self, figsize):
        """Set the size of the window plotting the figure.

        :param tuple figsize: the size of window to use.

        :TODO: remove the method and use the direct reference.

        """
        self.figsize = figsize

    def get_figsuptitle(self):
        """:returns: the main title of the plot.

        :TODO: remove the method and use the direct reference.

        """
        return self.figsuptitle

    def set_figsuptitle(self, suptitle):
        """Set the main title of the plot.

        :param str suptitle: the main title to use for the plot.

        :TODO: remove the method and use the direct reference.

        """
        self.figsuptitle = suptitle

    def set_to_plot(self, to_plot):
        """Set the figures plot.

        :param dict to_plot: description of the figures to plot.

        :TODO: remove the method and use a setter Python function.

        """
        self.to_plot = to_plot
        self.nb_to_plot = len(to_plot)

    def init_fig_subplot(self):
        """Initialize the figure and axes for the plot plot.

        """
        if self.nb_to_plot < 1:
            print("Error: nothing to plot")
            exit(1)
        nb_cols = int(np.ceil(np.sqrt(self.nb_to_plot)))
        nb_rows = int(np.ceil(self.nb_to_plot / nb_cols))
        self.fig, axe = plt.subplots(nb_rows, nb_cols, figsize=self.figsize)
        self.fig.suptitle(self.figsuptitle)
        self.axes = []
        if self.nb_to_plot == 1:
            self.axes.append(axe)
        elif self.nb_to_plot == 2:
            self.axes.append(axe[0])
            self.axes.append(axe[1])
        else:
            i = 0
            j = 0
            for k in range(self.nb_to_plot):
                self.axes.append(axe[i, j])
                i += 1
                if i == nb_rows:
                    j += 1
                    i = 0

    def set_titles(self):
        """Set the title of the figures from the to_plot dictionary.

        """
        if self.show_titles:
            for i, axe in enumerate(self.axes):
                if "title" in self.to_plot[i]:
                    axe.set_title(self.to_plot[i]["title"])

    def get_label_fontsize(self, to_plot, coord):
        """Extract the label font size of the coordinate from the to_plot dictionary. If there is not, returns 12.


        :param dict to_plot: the description of the plot.
        :param str coord: the axis of the label to get the font size.

        :returns: an integer which is the label font size parsed from the to_plot dictionnary.

        """
        param = "{}_label_fontsize".format(coord)
        if param in to_plot:
            return to_plot[param]
        else:
            return 12

    def get_xlabel_fontsize(self, to_plot):
        """Extract the label font size of the label on x axis parsed from the to_plot dictionnary.

        :param dict to_plot: the description of the plot.

        """
        return self.get_label_fontsize(to_plot, "x")

    def get_ylabel_fontsize(self, to_plot):
        """Extract the label font size of the label on y axis parsed from the to_plot dictionnary.

        :param dict to_plot: the description of the plot.

        """
        return self.get_label_fontsize(to_plot, "y")

    def set_labels(self):
        """Set the labels in the figures from the description of the plot.

        """
        for i, axe in enumerate(self.axes):
            if "x_label" in self.to_plot[i]:
                axe.set_xlabel(self.to_plot[i]["x_label"], fontsize=self.get_xlabel_fontsize(self.to_plot[i]))
            if "y_label" in self.to_plot[i]:
                axe.set_ylabel(self.to_plot[i]["y_label"], fontsize=self.get_ylabel_fontsize(self.to_plot[i]))

    def set_ticklabels(self):
        """Set the labels for the ticks and their font size in the figures.

        """
        for i, axe in enumerate(self.axes):
            if "x_ticklabels" in self.to_plot[i]:
                if "x_ticklabels_position" in self.to_plot[i]:
                    axe.set_xticks(self.to_plot[i]["x_ticklabels_position"])
                else:
                    ind = np.arange(0, len(self.to_plot[i]["x_ticklabels"]))
                    axe.set_xticks(ind)
                axe.set_xticklabels(self.to_plot[i]["x_ticklabels"])

            if "y_ticklabels" in self.to_plot[i]:
                if "y_ticklabels_position" in self.to_plot[i]:
                    axe.set_yticks(self.to_plot[i]["y_ticklabels_position"])
                else:
                    ind = np.arange(0, len(self.to_plot[i]["y_ticklabels"]))
                    axe.set_yticks(ind)
                axe.set_yticklabels(self.to_plot[i]["y_ticklabels"])

            if "x_ticklabels_fontsize" in self.to_plot[i]:
                for xticklabel in axe.get_xticklabels():
                    xticklabel.set_fontsize(self.to_plot[i]["x_ticklabels_fontsize"])

            if "y_ticklabels_fontsize" in self.to_plot[i]:
                for yticklabel in axe.get_yticklabels():
                    yticklabel.set_fontsize(self.to_plot[i]["y_ticklabels_fontsize"])

            if "ticklabels_fontsize" in self.to_plot[i]:
                axe.tick_params(labelsize=self.to_plot[i]["ticklabels_fontsize"])

    def set_grid(self):
        """Set the grid in the figures.

        """
        for i, axe in enumerate(self.axes):
            if "show_grid" in self.to_plot[i]:
                axe.grid(b=self.to_plot[i]["show_grid"])

    def get_bounds_and_norm(self, matrix):
        """Return the needed parameters for a clean colorbar for a Matrix plot.

        :param array matrix: the matrix to build a colorbar for.

        """
        if matrix.min() != matrix.max():
            bounds = np.linspace(
                int(matrix.min()),
                int(matrix.max()),
                int(matrix.max() - matrix.min()) + 1,
            )
            norm = mpl.colors.BoundaryNorm(
                np.arange(matrix.min() - 0.5, matrix.max() + 1 + 0.5, 1), self.cmap.N
            )
            return bounds, norm
        bounds = np.linspace(matrix.min() - 1, matrix.min() + 1, 3)
        norm = mpl.colors.BoundaryNorm(
            np.arange(matrix.min() - 0.5 - 1, matrix.max() + 1 + 0.5 + 1, 1),
            self.cmap.N,
        )
        return bounds, norm

    def remove_colorbars(self):
        """Remove the colorbars in the figures. Usefull for dynamic plot as colorbars are stacking while updating the plot.

        """
        if self.colorbars is not None:
            for colorbar in self.colorbars:
                colorbar.remove()
        self.colorbars = []

    def get_bar_width(self, to_plot):
        """Extract the bar width from the figure description.

        :param dict to_plot: the description of the figure.

        """
        if "bar_width" in to_plot:
            if (to_plot["bar_width"] > 0) and (to_plot["bar_width"] <= 1):
                return to_plot["bar_width"]
        return 0.8

    def get_multibar_width(self, to_plot):
        """Extract the bar width from the figure description.

        :param dict to_plot: the description of the figure.

        """
        if "bar_width" in to_plot:
            if (to_plot["bar_width"] > 0) and (to_plot["bar_width"] <= 1):
                return to_plot["bar_width"]
        return 0.6/len(to_plot["data"])

    def clean_plot(self):
        """Clean the figures before plotting. Usefull for dynamic plot.

        """
        self.remove_colorbars()

    def set_axe_properties(self):
        """Set information on the figures.

        """
        self.set_titles()
        self.set_labels()
        self.set_ticklabels()
        self.set_grid()

    def plot_matrix(self, to_plot, axe):
        """Compute the corresponding colorbar and plot a matrix.

        :param dict to_plot: the description of the figure.
        :param Axe axe: the subfigure where to plot the matrix.

        """
        bounds, norm = self.get_bounds_and_norm(to_plot["data"])
        mat = axe.matshow(to_plot["data"], cmap=self.cmap, norm=norm)
        colorbar = plt.colorbar(mat, ax=axe, ticks=bounds)
        if "colorbar_fontsize" in to_plot:
            colorbar.ax.tick_params(labelsize=to_plot["colorbar_fontsize"])
        if "colorbar_label" in to_plot:
                fontsize = 20
                if "colorbar_label_fontsize" in to_plot:
                    fontsize = to_plot["colorbar_label_fontsize"]
                colorbar.set_label(to_plot["colorbar_label"], fontsize=fontsize)
        self.colorbars.append(colorbar)

    def get_data_value_caract(self, to_plot):
        """:param dict to_plot: the description of the figure.

        :returns: the parameters for the data value to show in bar plot.

        """
        if "data_value_color" in to_plot:
            data_value_color = to_plot["data_value_color"]
        else:
            data_value_color = "w"

        if "data_value_fontsize" in to_plot:
            data_value_fontsize = to_plot["data_value_fontsize"]
        else:
            data_value_fontsize = 12

        return data_value_color, data_value_fontsize

    def show_text_value(self, to_plot, axe):
        """Add the values of bars as text.

        :param dict to_plot: the description of the figure.
        :param Axe axe: the subfigure where to show the values of data.

        """
        data_value_color, data_value_fontsize = self.get_data_value_caract(to_plot)
        for i, value in enumerate(to_plot["data"]):
            axe.text(
                i + 1,
                value / 2,
                "{:.2}".format(value),
                horizontalalignment="center",
                verticalalignment="center",
                color=data_value_color,
                fontsize=data_value_fontsize,
            )

    def plot_bar(self, to_plot, axe):
        """Compute the information and plot a bar figure.

        :param dict to_plot: the description of the figure.
        :param Axe axe: the subfigure where to plot the bars.

        """
        width = self.get_bar_width(to_plot)
        axe.bar(np.arange(1, len(to_plot["data"]) + 1), to_plot["data"], width=width)
        show_data_value = False
        if "show_data_value" in to_plot:
            if to_plot["show_data_value"]:
                self.show_text_value(to_plot, axe)
        if "rotate_x_labels" in to_plot:
            if to_plot["rotate_x_labels"]:
                plt.setp(axe.get_xticklabels(), rotation=30, ha='right')

    def plot_multibar(self, to_plot, axe):
        """Compute the information and plot a multibar figure.

        :param dict to_plot: the description of the figure.
        :param Axe axe: the subfigure where to plot the bars.

        """
        n = len(to_plot["data"])
        w = self.get_multibar_width(to_plot)
        for i, data in enumerate(to_plot["data"]):
            x_pos = [x + 1 + 2*w*n - (n*w/2) + ( (2*i+1)*(w/2) ) for x in range(len(data)) ]
            if "colors" in to_plot:
                axe.bar(x_pos, data, width=w, align="center", color=to_plot["colors"][i])
            else:
                axe.bar(x_pos, data, width=w, align="center")
            ind = [x + 1 + 2*w*n for x in range(len(to_plot["x_ticklabels"]))]
            axe.set_xticks(ind)

    def add_legend(self, to_plot, axe):
        """Add a legend to the figure.

        :param dict to_plot: the description of the figure.
        :param Axe axe: the subfigure where to add the legend.

        """
        if "legend" in to_plot:
            axe.legend(to_plot["legend"])

    def plot_pie(self, to_plot, axe):
        """Compute the information and plot a pie figure.

        :param dict to_plot: the description of the figure.
        :param Axe axe: the subfigure where to plot the pie.

        """
        labels = None
        if "labels" in to_plot:
            labels = to_plot["labels"]
        axe.pie(to_plot["data"], autopct='%3.2f%%', labels=labels)

    def plot_multiscatter(self, to_plot, axe):
        """Compute the information and plot a multiple scatter figure.

        :param dict to_plot: the description of the figure.
        :param Axe axe: the subfigure where to plot the pie.

        """
        x_coef, y_coef = self.add_scatter_image(to_plot, axe)
        opacity = self.get_opacity(to_plot)
        for data in to_plot["data"]:
            x_data = [d*x_coef for d in data[0]]
            y_data = [d*y_coef for d in data[1]]
            axe.scatter(x_data, y_data, alpha=opacity)

    def matrix_to_scatter(self, matrix):
        """Convert the given matrix to data for scatter. Every value in the matrix will correspond to a set of data and can be plot in a multiscatter figure.

        :param array matrix: the matrix to convert into a scatter.

        """
        dim = matrix.shape
        values = []
        values_pos = []
        for x in range(dim[0]):
            for y in range(dim[1]):
                value = matrix[x][y]
                if value != 0:
                    if not value in values:
                        values.append(value)
                        values_pos.append([[],[]])
                    value_index = values.index(value)
                    values_pos[value_index][0].append(x)
                    values_pos[value_index][1].append(y)
        return values, values_pos

    def redim_axe(self, shape, axe):
        """Redimension the figure with the given shape.

        :param tuple shape: the target width and height of the figure.
        :param Axe axe: the subfigure to work on.

        """
        x_size = shape[1]
        y_size = shape[0]
        axe.set_ylim((0, y_size))
        axe.set_xlim((0, x_size))

    def add_image_to_axe(self, to_plot, axe):
        """Add the image from the figure description as a background.

        Arguments:

        to_plot - the dictionnary to parse for getting information.

        axe - the subfigure to work on.

        """
        if "image" in to_plot:
            img = plt.imread(to_plot["image"])
            axe.imshow(img)
            self.redim_axe(img.shape, axe)
            return img.shape

    def revert_axes(self, to_plot, axe):
        """Change the orientation of the axis.

        Arguments:

        to_plot - the dictionnary to parse for getting information.

        axe - the subfigure to work on.

        """
        if "revert_axis" in to_plot:
            if to_plot["revert_axis"]:
                axe.set_xlin(axe.get_xlim()[::-1])
                axe.set_ylim(axe.get_ylim()[::-1])
        else:
            if "revert_y_axis" in to_plot:
                if to_plot["revert_y_axis"]:
                    axe.set_ylim(axe.get_ylim()[::-1])
            if "revert_x_axis" in to_plot:
                if to_plot["revert_x_axis"]:
                    axe.set_xlin(axe.get_xlim()[::-1])

    def get_opacity(self, to_plot):
        if "opacity" in to_plot:
            return to_plot["opacity"]
        else:
            return 1

    def add_scatter_image(self, to_plot, axe):
        """Add the image given in to_plot as a background for the axe. Works only for
        scatter type figures.

        Arguments:

        to_plot - the dictionnary to parse for getting information.

        axe - the subfigure where to work on.

        """
        x_coef = 1
        y_coef = 1
        if "image" in to_plot:
            img_shape = self.add_image_to_axe(to_plot, axe)
            if "scale_to_image" in to_plot:
                if to_plot["scale_to_image"]:
                    img_width = img_shape[1]
                    img_height = img_shape[0]
                    mat_width = to_plot["data"].shape[1]-1
                    mat_height = to_plot["data"].shape[0]-1
                    x_coef = img_width/mat_width
                    y_coef = img_height/mat_height
                if "x_scale" in to_plot:
                    x_coef = x_coef*to_plot["x_scale"]
                if "y_scale" in to_plot:
                    y_coef = y_coef*to_plot["y_scale"]
        return x_coef, y_coef

    def plot_matrixscatter(self, to_plot, axe):
        """Plot the data from to_plot as a matrix in a scatter style with the corresponding colorbar.

        Arguments:

        to_plot - the dictionnary to parse for getting information.

        axe - the subfigure where to work on.

        """
        x_coef, y_coef = self.add_scatter_image(to_plot, axe)
        values, values_pos = self.matrix_to_scatter(to_plot["data"])
        mini = 0
        if len(values) > 0:
            maxi = max(values)
            bounds = np.arange(0, maxi+1)
            norm = mpl.colors.BoundaryNorm(np.arange(mini-0.5, maxi+0.5+1, 1), self.cmap.N)
            opacity = self.get_opacity(to_plot)
            for value, data in zip(values, values_pos):
                c_array = [value]*len(data[0])
                x_data = [d*x_coef for d in data[1]]
                y_data = [d*y_coef for d in data[0]]
                scat = axe.scatter(x_data, y_data, c=c_array, vmax=maxi,
                                   vmin=mini, cmap=self.cmap, norm=norm,
                                   alpha=opacity)
            colorbar = plt.colorbar(scat, ax=axe, ticks=bounds)
            if "colorbar_fontsize" in to_plot:
                colorbar.ax.tick_params(labelsize=to_plot["colorbar_fontsize"])
            if "colorbar_label" in to_plot:
                fontsize = 20
                if "colorbar_label_fontsize" in to_plot:
                    fontsize = to_plot["colorbar_label_fontsize"]
                colorbar.set_label(to_plot["colorbar_label"], fontsize=fontsize)
            self.colorbars.append(colorbar)

    def plot_scatter(self, to_plot, axe):
        """Plot the data from to_plot as a scatter.

        Arguments:

        to_plot - the dictionnary to parse for getting information.

        axe - the subfigure where to work on.

        """
        x_coef, y_coef = self.add_scatter_image(to_plot, axe)
        data = to_plot["data"]
        x_data = [d*x_coef for d in data[0]]
        y_data = [d*y_coef for d in data[1]]
        opacity = self.get_opacity(to_plot)
        axe.scatter(x_data, y_data, alpha=opacity)

    def plot_data(self):
        """Plot the data from the to_plot parameter.

        """
        self.clean_plot()
        self.set_axe_properties()
        for i, axe in enumerate(self.axes):
            to_plot = self.to_plot[i]
            if to_plot["type"] == "matrix" or to_plot["type"] == PlotterType.MATRIX:
                self.plot_matrix(to_plot, axe)
            elif to_plot["type"] == "scatter" or to_plot["type"] == PlotterType.SCATTER:
                self.plot_scatter(to_plot, axe)
            elif to_plot["type"] == "histogram" or to_plot["type"] == PlotterType.HISTOGRAM:
                axe.hist(to_plot["data"])
            elif to_plot["type"] == "trace" or to_plot["type"] == PlotterType.TRACE:
                axe.plot(to_plot["data"])
            elif to_plot["type"] == "plot" or to_plot["type"] == PlotterType.PLOT:
                axe.plot(to_plot["data"][0], to_plot["data"][1])
            elif (to_plot["type"] == "multitrace" or to_plot["type"] == PlotterType.MULTITRACE):
                for data in to_plot["data"]:
                    axe.plot(data)
            elif to_plot["type"] == "bar" or to_plot["type"] == PlotterType.BAR:
                self.plot_bar(to_plot, axe)
            elif to_plot["type"] == "multibar" or to_plot["type"] == PlotterType.MULTIBAR:
                self.plot_multibar(to_plot, axe)
            elif to_plot["type"] == "pie" or to_plot["type"] == PlotterType.PIE:
                self.plot_pie(to_plot, axe)
            elif to_plot["type"] == "multiscatter" or to_plot["type"] == PlotterType.MULTISCATTER:
                self.plot_multiscatter(to_plot, axe)
            elif to_plot["type"] == "matrixscatter" or to_plot["type"] == PlotterType.MATRIXSCATTER:
                self.plot_matrixscatter(to_plot, axe)
            self.add_legend(to_plot, axe)
            self.revert_axes(to_plot, axe)

    def export_tikz(self, filename="tikz_fig.tex"):
        """Export the figure to a tikz file. This method cannot be called after the
        show() method otherwise the result file will not containing the figure.

        Arguments:

        filename - the path to the file where to store the tikz description of
        the figure (default: "tikz_fig.tex").

        """
        self.plot_data()
        tikz_save(filename)

    def clean_axes(self):
        """Clean axes. Usefull for dynamic plot.

        """
        for axe in self.axes:
            axe.cla()

    def show(self, blocking=True):
        """Show the figure.

        Arguments:

        blocking - if set to True, the program will stall on this function
        while the window is remained opened (default: True).

        """
        if blocking:
            self.plot_data()
            if self.tikz_export:
                tikz_save(self.tikz_file)
            plt.show()
        else:
            self.clean_axes()
            self.plot_data()
            plt.pause(0.1)

    def init_plot(self):
        """Initialize the plot.

        """
        self.init_fig_subplot()

    def set_axes_aspect(self):
        """Adapt the aspect of the subfigures. Usefull when a subfigure type of plot is
        changing, like in the Gtk3 example for instance.

        """
        for axe in self.axes:
            axe.set_aspect("auto")
