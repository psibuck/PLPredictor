from os import system
from collections import namedtuple
from tkinter import *
from functools import partial
import sys, termios, tty, os, time

from code.standings_panel import *
from code.league_table_panel import *
from code.add_user_panel import *

class Predictor:

    def __init__(self, root):
        self.root = root
        self.selected_panel = IntVar()
        self.selected_panel.set( 1 )

        nav_area = Frame(self.root)
        nav_area.pack(side=TOP)

        panel_area = Frame(self.root)
        panel_area.pack(side=BOTTOM, fill=BOTH, expand=True)

        self.frames = {}
        for panel in (Standings, LeagueTable, AddUser):

            new_frame = panel(parent=panel_area, controller=self.root)

            name = new_frame.get_name()
            self.frames[name] = new_frame
            new_frame.grid(row=0,column=0,sticky="nsew")
            
            func_with_args = partial(self.select_panel, name)
            Radiobutton(self.root, text=name, indicatoron=0, padx=20, command=func_with_args,
                         value=name).pack(in_=nav_area, side=LEFT)

        self.select_panel( Standings.get_name() )
    
    def select_panel(self, panel_name):
        frame = self.frames[panel_name]
        frame.tkraise()


def main():
    root = Tk()
    root.title( "Premier League Predictor" )
    root.minsize(400,600)

    app = Predictor( root )

    root.configure(background="green")
    root.mainloop()

main()