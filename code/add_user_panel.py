from tkinter import Frame, PhotoImage
import tkinter as tk
import os
from os import path
from functools import partial

data_folder = os.path.dirname(__file__) + '/../data'
league_path = data_folder + '/local/league_table.txt'
users_path = data_folder + '/local/users/'

# Draws the current league table to the screen
class AddUser(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.up_image = PhotoImage( file=(data_folder + '/icons/up-arrow.png')).subsample(25,25)
        self.down_image = PhotoImage( file=(data_folder + '/icons/down-arrow.png')).subsample(25,25)

        button_frame = tk.Frame(self)
        button_frame.grid(row=0,column=0,sticky="nsew")

        if path.exists( league_path ):
            self.table = tk.Frame(self)
            self.table.bg = "blue"
            self.table.grid(row=1,column=0,sticky="nsew")

            self.read_standings()
            self.setup_table()

            self.username = tk.Entry(button_frame)
            self.username.grid(row=0, column=1)
            self.username.focus()

            add_team_button = tk.Button(button_frame, text="Add User", command=self.add_user)
            add_team_button.grid(row=0, column=2)  
        else:
            error_label = tk.Label(text="Cannot add users until you have created a league")
            error_label.grid(row=0, column=1)

    def read_standings(self):
        self.standings = []
        with open(league_path, 'r' ) as filedata:
            for line in filedata:
                self.standings.append( line.rstrip('\n') )

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

    def add_user(self):
        save_file = open(users_path + str(self.username.get()) + ".txt", "w+")
        for line in self.standings:
            save_file.write(str(line) + '\n')
        save_file.close()
        self.username.delete(0,'end')

    def swap_positions(self, pos1, pos2 ):
        copy = self.standings[pos1]
        self.standings[pos1] = self.standings[pos2]
        self.standings[pos2] = copy
        self.setup_table()

    @staticmethod
    def get_name():
        return "Add User"


