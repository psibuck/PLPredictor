import os

class User:

    def __init__(self, name, filepath="" ):
        self.name = name
        self.team_list = []
        self.filepath = filepath
        self.score = 0

    def load(self):
        data = open(self.filepath)
        count = 0
        for line in data:
            self.team_list.append( line )
            count = count + 1

    def create(self):
        filepath = os.path.dirname(__file__) + '/../data/users/' + str( self.name ) + '.txt'
        file = open( filepath, "w")
        for team in self.team_list:
            file.write( str( team ) + '\n' )
        file.close() 

