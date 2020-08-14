from tkinter import Frame
import tkinter as tk

from os import path

data_path = '/../data/league_table.txt'

# Draws the current league table to the screen
class AddUser(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the Add User Page")
        label.pack(side="top", fill="x", pady=10)

        if path.exists( data_path ):
            league_table = open(os.path.dirname(__file__) +  data_path )
            for line in league_table:
                print( line )

    @staticmethod
    def get_name():
        return "Add User"

