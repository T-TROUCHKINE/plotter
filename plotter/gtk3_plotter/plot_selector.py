import sys
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import GLib, Gtk, GObject

from plotter import Plotter

from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas
import numpy as np
import threading
import time


class PlotSelector(Gtk.Box):
    def __init__(self, figs, update_func=None):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.figs = figs
        self.cur_fig = 0
        self.update_func = update_func
        self.update_fig = True

        self.__build_gui()

        if update_func != None:
            self.__start_fig_idle()

    def set_figs(self, figs):
        self.figs = figs
        self.__update_fig()

    def __build_gui(self):
        self.set_border_width(10)

        if self.update_func != None:
            self.stop_btn = self.__create_stop_btn()

        self.canvas = self.__create_canvas()
        self.cb = self.__create_combo_box()
        self.sw = Gtk.ScrolledWindow()
        self.btn_box = Gtk.Box(spacing=6)

        if self.update_func != None:
            self.btn_box.pack_start(self.stop_btn, False, False, 0)
        self.btn_box.pack_start(self.cb, False, False, 0)
        self.sw.add(self.canvas)

        self.pack_start(self.btn_box, False, False, 0)
        self.pack_start(self.sw, True, True, 0)

    def __create_stop_btn(self):
        stop_btn = Gtk.ToggleButton(label="Stop")
        stop_btn.connect("toggled", self.__on_stop_btn_toggled)
        return stop_btn

    def __on_stop_btn_toggled(self, btn):
        if btn.get_active():
            self.update_fig = False
        else:
            self.update_fig = True

    def __create_combo_box(self):
        figs_store = Gtk.ListStore(int, str)
        for i, fig in enumerate(self.figs):
            elem = [i, fig["title"]]
            figs_store.append(elem)
        cb = Gtk.ComboBox.new_with_model(figs_store)
        cb.connect("changed", self.__on_cb_changed)
        cb.set_entry_text_column(1)
        cb.set_active(self.cur_fig)
        renderer_text = Gtk.CellRendererText()
        cb.pack_start(renderer_text, True)
        cb.add_attribute(renderer_text, "text", 1)
        return cb

    def __on_cb_changed(self, cb):
        tree_iter = cb.get_active_iter()
        if tree_iter is not None:
            model = cb.get_model()
            self.cur_fig = model[tree_iter][0]
            self.__update_fig()

    def __init_fig(self):
        self.pl = Plotter([self.figs[self.cur_fig]])
        self.pl.init_plot()
        self.pl.plot_data()
        self.pl.set_show_titles(False)
        return self.pl.get_fig()

    def __create_canvas(self):
        fig = self.__init_fig()
        canvas = FigureCanvas(fig)
        canvas.set_size_request(400, 300)
        return canvas

    def __update_fig(self, update=True):
        if update:
            if self.update_func != None:
                self.figs[self.cur_fig]["data"] = self.update_func(self.cur_fig)
            self.pl.set_to_plot([self.figs[self.cur_fig]])
            self.pl.clean_axes()
            self.pl.plot_data()
            self.pl.set_axes_aspect()
            self.pl.get_fig().tight_layout()
            self.canvas.draw()

    def __fig_idle(self):
        while 1:
            GLib.idle_add(self.__update_fig, self.update_fig)
            time.sleep(0.4)

    def __start_fig_idle(self):
        thread = threading.Thread(target=self.__fig_idle)
        thread.daemon = True
        thread.start()
