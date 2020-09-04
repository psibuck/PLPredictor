# PLPredictor
A simple gui application that allows an admin to manager a mini-league predictor game.

The GUI is written using Tkinter. 

Players entries are stored in a named data folder where the name of the file(.txt) is the username and the data contained inside the file is their prediction. 

These entries are then collated into a leaderboard. Points are added for each position a users prediction differs from the real table. Then the user with the lowest par score is considered better.

In the event of a draw it is decided as follows:
- user with most correct positions(0 scores)
- user that predicted correct from top of the table down(e.g first discrepancy between the two)

All icons are made by Pixel perfect from www.flaticon.com
