import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib2tikz import save as tikz_save
from enum import Enum

class PlotterType(Enum):
    MATRIX = 1
    SCATTER = 2
    HISTOGRAM = 3
    TRACE = 4
    PLOT = 5
    MULTITRACE = 6
    BAR = 7
    MULTIBAR = 8

class Plotter:
    def __init__(self, to_plot, figsuptitle=None, figsize=(20, 20), tikz_file=""):
        self.figsize = figsize
        self.figsuptitle = figsuptitle
        self.fig = None

        if isinstance(to_plot, int):
            self.nb_to_plot = to_plot
            self.to_plot = None
        elif to_plot is not None:
            self.to_plot = to_plot
            self.nb_to_plot = len(self.to_plot)

        self.axes = None
        self.colorbars = None
        self.cmap = plt.cm.jet
        self.show_titles = True

        self.tikz_export = False
        if len(tikz_file) > 0:
            self.tikz_file = tikz_file
            self.tikz_export = True

        self.init_plot()

    def set_show_titles(self, val):
        self.show_titles = val

    def get_fig(self):
        return self.fig

    def set_colormap(self, cmap):
        self.cmap = cmap

    def get_figsize(self):
        return self.figsize

    def set_figsize(self, figsize):
        self.figsize = figsize

    def get_figsuptitle(self):
        return self.figsuptitle

    def set_figsuptitle(self, suptitle):
        self.figsuptitle = suptitle

    def set_to_plot(self, to_plot):
        self.to_plot = to_plot
        self.nb_to_plot = len(to_plot)

    def init_fig_subplot(self):
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
        if self.show_titles:
            for i, axe in enumerate(self.axes):
                if "title" in self.to_plot[i]:
                    axe.set_title(self.to_plot[i]["title"])

    def get_label_fontsize(self, to_plot, coord):
        param = "{}_label_fontsize".format(coord)
        if param in to_plot:
            return to_plot[param]
        else:
            return 12

    def get_xlabel_fontsize(self, to_plot):
        return self.get_label_fontsize(to_plot, "x")

    def get_ylabel_fontsize(self, to_plot):
        return self.get_label_fontsize(to_plot, "y")

    def set_labels(self):
        for i, axe in enumerate(self.axes):
            if "x_label" in self.to_plot[i]:
                axe.set_xlabel(self.to_plot[i]["x_label"], fontsize=self.get_xlabel_fontsize(self.to_plot[i]))
            if "y_label" in self.to_plot[i]:
                axe.set_ylabel(self.to_plot[i]["y_label"], fontsize=self.get_ylabel_fontsize(self.to_plot[i]))

    def set_ticklabels(self):
        for i, axe in enumerate(self.axes):
            fontdict = None
            if "x_ticklabels" in self.to_plot[i]:
                ind = np.arange(1, len(self.to_plot[i]["x_ticklabels"]) + 1)
                axe.set_xticks(ind)
                if "x_ticklabels_fontsize" in self.to_plot[i]:
                    fontdict = {"fontsize": self.to_plot[i]["x_ticklabels_fontsize"]}
                axe.set_xticklabels(self.to_plot[i]["x_ticklabels"], fontdict)
            if "y_ticklabels_fontsize" in self.to_plot[i]:
                for yticklabel in axe.get_yticklabels():
                    yticklabel.set_fontsize(self.to_plot[i]["y_ticklabels_fontsize"])
            if "ticklabels_fontsize" in self.to_plot[i]:
                axe.tick_params(labelsize=self.to_plot[i]["ticklabels_fontsize"])

    def set_grid(self):
        for i, axe in enumerate(self.axes):
            if "show_grid" in self.to_plot[i]:
                axe.grid(b=self.to_plot[i]["show_grid"])

    def get_bounds_and_norm(self, matrix):
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
        if self.colorbars is not None:
            for colorbar in self.colorbars:
                colorbar.remove()
        self.colorbars = []

    def get_bar_width(self, to_plot):
        if "bar_width" in to_plot:
            if (to_plot["bar_width"] > 0) and (to_plot["bar_width"] <= 1):
                return to_plot["bar_width"]
        return 0.8

    def clean_plot(self):
        self.remove_colorbars()

    def set_informations(self):
        self.set_titles()
        self.set_labels()
        self.set_ticklabels()
        self.set_grid()

    def plot_matrix(self, to_plot, axe):
        bounds, norm = self.get_bounds_and_norm(to_plot["data"])
        mat = axe.matshow(to_plot["data"], cmap=self.cmap, norm=norm)
        colorbar = plt.colorbar(mat, ax=axe, ticks=bounds)
        if "colorbar_fontsize" in to_plot:
            colorbar.ax.tick_params(labelsize=to_plot["colorbar_fontsize"])
        self.colorbars.append(colorbar)

    def get_data_value_caract(self, to_plot, axe):
        if "data_value_color" in to_plot:
            data_value_color = to_plot["data_value_color"]
        else:
            data_value_color = "w"

        if "data_value_fontsize" in to_plot:
            data_value_fontsize = to_plot["data_value_fontsize"]
        else:
            data_value_fontsize = 12

        if "rotate_x_labels" in to_plot:
            if to_plot["rotate_x_labels"]:
                axe.autofmt_xdate()

        return data_value_color, data_value_fontsize

    def show_text_value(self, to_plot, axe):
        data_value_color, data_value_fontsize = self.get_data_value_caract(to_plot, axe)
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
        width = self.get_bar_width(to_plot)
        axe.bar(np.arange(1, len(to_plot["data"]) + 1), to_plot["data"], width=width)
        show_data_value = False
        if "show_data_value" in to_plot:
            if to_plot["show_data_value"]:
                self.show_text_value(to_plot, axe)

    def plot_multibar(self, to_plot, axe):
        w = self.get_bar_width(to_plot)
        for i, data in enumerate(to_plot["data"]):
            n = len(to_plot["data"])
            x_pos = [x + 1 + 2*w*n - (n*w/2) + ( (2*i+1)*(w/2) ) for x in range(len(data)) ]
            if "colors" in to_plot:
                axe.bar(x_pos, data, width=w, align="center", color=to_plot["colors"][i])
            else:
                axe.bar(x_pos, data, width=w, align="center")
            ind = [x + 1 + 2*w*n for x in range(len(to_plot["x_ticklabels"]))]
            axe.set_xticks(ind)

    def add_legend(self, to_plot, axe):
        if "legend" in to_plot:
            axe.legend(to_plot["legend"])

    def plot_data(self):
        self.clean_plot()
        self.set_informations()
        for i, axe in enumerate(self.axes):
            to_plot = self.to_plot[i]
            if to_plot["type"] == "matrix" or to_plot["type"] == PlotterType.MATRIX:
                self.plot_matrix(to_plot, axe)
            elif to_plot["type"] == "scatter" or to_plot["type"] == PlotterType.SCATTER:
                axe.scatter(to_plot["data"][0], to_plot["data"][1])
            elif (
                to_plot["type"] == "histogram"
                or to_plot["type"] == PlotterType.HISTOGRAM
            ):
                axe.hist(to_plot["data"])
            elif to_plot["type"] == "trace" or to_plot["type"] == PlotterType.TRACE:
                axe.plot(to_plot["data"])
            elif to_plot["type"] == "plot" or to_plot["type"] == PlotterType.PLOT:
                axe.plot(to_plot["data"][0], to_plot["data"][1])
            elif (
                to_plot["type"] == "multitrace"
                or to_plot["type"] == PlotterType.MULTITRACE
            ):
                for data in to_plot["data"]:
                    axe.plot(data)
            elif to_plot["type"] == "bar" or to_plot["type"] == PlotterType.BAR:
                self.plot_bar(to_plot, axe)
            elif to_plot["type"] == "multibar" or to_plot["type"] == PlotterType.MULTIBAR:
                self.plot_multibar(to_plot, axe)
            self.add_legend(to_plot, axe)

    def export_tikz(self, filename="tikz_fig.tex"):
        self.plot_data()
        tikz_save(filename)

    def clean_axes(self):
        for axe in self.axes:
            axe.cla()

    def show(self, blocking=True):
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
        self.init_fig_subplot()

    def set_axes_aspect(self):
        for axe in self.axes:
            axe.set_aspect("auto")
