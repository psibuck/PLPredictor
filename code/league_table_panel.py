from tkinter import Frame, PhotoImage, Label
from functools import partial
import tkinter as tk

import os
from os import path

data_folder = os.path.dirname(__file__) + '/../data'
league_path = data_folder + '/local/league_table.txt'

# Draws the current league table to the screen
class LeagueTable(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.num_teams = 0
        self.edited = False
        self.standings = []
        self.up_image = PhotoImage( file=(data_folder + '/icons/up-arrow.png')).subsample(25,25)
        self.down_image = PhotoImage( file=(data_folder + '/icons/down-arrow.png')).subsample(25,25)
        self.delete_image = PhotoImage( file=(data_folder + '/icons/delete.png')).subsample(25,25)

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

        self.save_button = tk.Button(button_frame, text="Save Changes", command=self.save_changes)
        self.save_button.grid(row=0,column=3)
        self.discard_button = tk.Button(button_frame, text="Discard Changes", command=self.discard_changes)
        self.discard_button.grid(row=0, column=4)

        self.no_changes_state()

        if path.exists( league_path ):
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
                up_button = tk.Button(row,image=self.up_image, command=swap_up_command)
                up_button.grid(row=0,column=3)
            if self.num_teams < len(self.standings):
                swap_down_command = partial(self.swap_positions, self.num_teams - 1, self.num_teams)
                down_button = tk.Button(row, image=self.down_image,command=swap_down_command)
                down_button.grid(row=0,column=4)

            delete_entry_command = partial(self.delete_entry, self.num_teams - 1)
            delete_button = tk.Button(row, image=self.delete_image, command=delete_entry_command)
            delete_button.grid(row=0, column=5)
    
    def delete_entry(self,pos):
        self.changes_made_state()
        self.standings.pop(pos)
        self.setup_table()

    def read_standings(self):
        self.standings = []
        with open(league_path, 'r' ) as filedata:
            for line in filedata:
                self.standings.append( line.rstrip('\n') )
    
    def swap_positions(self, pos1, pos2 ):
        self.changes_made_state()
        copy = self.standings[pos1]
        self.standings[pos1] = self.standings[pos2]
        self.standings[pos2] = copy
        self.setup_table()

    def add_team(self):
        self.changes_made_state()
        self.standings.append(self.team_name_entry.get())
        self.team_name_entry.delete(0,'end')
        self.setup_table()

    def changes_made_state(self):
        self.save_button["state"]= "normal"
        self.discard_button["state"]= "normal"

    def no_changes_state(self):
        self.save_button["state"]= "disabled"
        self.discard_button["state"]= "disabled"

    def discard_changes(self):
        self.no_changes_state()
        self.read_standings()
        self.setup_table()

    def save_changes(self):
        self.no_changes_state()
        save_file = open(league_path, "w+")
        for line in self.standings:
            save_file.write(str(line) + '\n')
        save_file.close()

    @staticmethod
    def get_name():
        return "League Table"

