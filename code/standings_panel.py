from .loader import get_league_table
from .user import *
import os, glob
from os import system

from tkinter import Frame
import tkinter as tk

class Standings(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the Standings Page")
        label.pack(side="top", fill="x", pady=10)

    @staticmethod
    def get_name():
        return "Standings"


    def draw_standings(self):
        data_location = os.path.dirname(__file__) + '/../data/users/'
        users = []
        for file in glob.glob(os.path.join( data_location, '*.txt' )):
            filename = os.path.basename(file)
            new_user = User( filename[:-4], file )
            new_user.load()
            users.append( new_user )

        league_table = get_league_table()

        for user in users:
            user.score = 0
            position = 0
            for team in user.team_list:
                league_position = league_table.index( team.rstrip() )
                user.score = user.score + abs( league_position - position )
                position = position + 1


        place = 1
        users.sort(key=lambda x: x.score, reverse=False)
        for user in users:
            spaces = (8 - len( user.name )) * ' '
            print( '\033[92m' + str(place) + ". "  + user.name + str(spaces) + ": " + str( user.score ) + "pts" )
            place = place + 1

