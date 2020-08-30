from tkinter import Frame
import tkinter as tk

# Draws the current league table to the screen
class AddUser(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the Add User Page")
        label.pack(side="top", fill="x", pady=10)

    @staticmethod
    def get_name():
        return "Add User"

