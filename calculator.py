#!/usr/bin/python3
'''A simple calculator application.'''

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from evaluator import Expression



class CalculatorWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='Calculator')
        self.set_size_request(300, 100)
        self.set_resizable(False)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(vbox)

        self.entry = Gtk.Entry()
        vbox.pack_start(self.entry, True, True, 0)

        self.button = Gtk.Button()
        self.button.set_label('Calculate')
        self.button.connect('clicked', self.on_evaluate_clicked)
        vbox.pack_start(self.button, True, True, 0)

    def on_evaluate_clicked(self, button):
        expression_string = self.entry.get_text()
        expression_value = Expression(expression_string).eval()
        self.entry.set_text(str(expression_value))

def main():
    window = CalculatorWindow()
    window.connect('delete-event', Gtk.main_quit)
    window.show_all()
    Gtk.main()

if __name__ == '__main__':
    main()
