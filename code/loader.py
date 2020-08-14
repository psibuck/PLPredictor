import json, os

def load_teams():
    data = json.load( open(os.path.dirname(__file__) + '/../data/unique_ids.json') )
    return data

def get_league_table():
    count = 0
    teams = []
    data = open(os.path.dirname(__file__) + '/../data/league_table.txt')
    for line in data:
        teams.append( line.rstrip() )
        count = count + 1
    return teams





