import sys
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import GLib, Gtk, GObject

import numpy as np

from plotter.gtk3_plotter import PlotSelector

"""
Figures to plot with initial values
"""
mat = np.random.random((100, 100))
trace = np.random.random(100)
to_plot = [
    {
        "title": "Matrix",
        "type": "matrix",
        "data": mat
    },
    {
        "title": "Trace",
        "type": "trace",
        "data": trace},
]

"""
Update function Depending of the value of "fig" which select the figure to
plot, the function return the data to plot
"""
def update_fig(fig):
    if fig == 0:
        return np.random.random((100, 100))
    elif fig == 1:
        return np.random.random(100)
    else:
        return None

ps = PlotSelector(to_plot, update_fig)

win = Gtk.Window()
win.connect("delete-event", Gtk.main_quit)
win.set_default_size(400, 400)
win.set_title("Embedding in GTK")
win.add(ps)
win.show_all()
Gtk.main()
