from tkinter import Frame
from functools import partial
import tkinter as tk

import os
from os import path

filepath = os.path.dirname(__file__) + '/../data/league_table.txt'

# Draws the current league table to the screen
class LeagueTable(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.num_teams = 0
        self.standings = []

        self.table = tk.Frame(self)
        self.table.bg = "blue"
        self.table.grid(row=1,column=0,sticky="nsew")

        button_frame = tk.Frame(self)
        button_frame.grid(row=0,column=0,sticky="nsew")

        self.team_name_entry = tk.Entry(button_frame)
        self.team_name_entry.grid(row=0, column=1)
        self.team_name_entry.focus()

        add_team_button = tk.Button(button_frame, text="Add Team", command=self.add_team)
        add_team_button.grid(row=0, column=2)  

        print("test")
        if path.exists( filepath ):
            self.read_standings()
            self.setup_table()

    def setup_table(self):
        self.num_teams = 0
        self.table.destroy()
        self.table = tk.Frame(self)
        self.table.configure( background="blue" )
        self.table.grid(row=1, column=0, sticky="nsew")

        for team in self.standings:
            self.num_teams = self.num_teams + 1

            row = tk.Frame(self.table)
            row.grid(row=self.num_teams,sticky="ew", pady=5)

            count_label = tk.Label(row, text=self.num_teams)
            count_label.grid(row=0,column=1)
            if self.num_teams < 5:
                count_label.configure(background="gold")
            elif self.num_teams > 17:
                count_label.configure(background="red")

            label = tk.Label(row, text=team)
            label.grid(row=0,column=2)

            if self.num_teams > 1:
                swap_up_command = partial(self.swap_positions, self.num_teams - 1, self.num_teams - 2)
                up_button = tk.Button(row, text="UP", command=swap_up_command)
                up_button.grid(row=0,column=3)
            if self.num_teams < len(self.standings):
                swap_down_command = partial(self.swap_positions, self.num_teams - 1, self.num_teams)
                down_button = tk.Button(row, text="DOWN",command=swap_down_command)
                down_button.grid(row=0,column=4)
 
    def read_standings(self):
        with open(filepath, 'r' ) as filedata:
            print( filedata )
            for line in filedata:
                self.standings.append( line )
    
    def swap_positions(self, pos1, pos2 ):
        copy = self.standings[pos1]
        self.standings[pos1] = self.standings[pos2]
        self.standings[pos2] = copy
        self.setup_table()


    def write_standings(self):
        file = open( filepath, 'w' )
        if file:
            for team in self.standings:
                file.write( team )

    def add_team(self):
        self.standings.append(self.team_name_entry.get())
        self.team_name_entry.delete(0,'end')
        self.setup_table()

    @staticmethod
    def get_name():
        return "League Table"

