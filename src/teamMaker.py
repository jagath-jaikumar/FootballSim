import json

from lib.player import Player

def loadPlayers():
    with open('data/py_objects/M20_players.json') as json_file:
        data = json.load(json_file)
        players = []


    return data

def main():
    players = loadPlayers()
    teams = {}
    for p in players:
        if p['Team'] in teams:
            teams[p['Team']].append(p)
        else:
            teams[p['Team']] = [p]
    
    for team in teams:
        filename = 'data/py_objects/' + str(team) + '.json'
        with open(filename, 'w') as f:
            json.dump(teams[team], f, indent=4, separators=(',', ': '),sort_keys=True)



if __name__ == "__main__":
    main()