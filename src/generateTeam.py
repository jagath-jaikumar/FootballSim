from lib.player import Player
from lib.team import Team 
import sys
import json

def main():
    teams = ['ari','atl','bal','buf','car','chi','cin','cle','dal', 'den', 'det', 'gb', 'hou', 'ind','jax','kc', 'lac', 'lar', 'lv','mia','min','ne','no','nyg','nyj','phi','pit','sea','sf','tb','ten','was']

    gotTeam = False
    team = ""
    while (not gotTeam):
        try:
            team = input("Enter a team abbreviation\n")
            team = team.lower()
            if team == 'q' or team == '^C':
                raise Exception('q')
            elif team not in teams:
                raise Exception('bad')
            else:
                gotTeam = True
        except Exception as e:
            if str(e) == 'q':
                sys.exit(0)
            else:
                print("Invalid team name")

    team = team.upper()

    filename = 'data/py_objects/'+team+'.json'
    data = []
    with open(filename) as json_file:
        data = json.load(json_file)

    
    players = []
    for d in data:
        p = Player(d)
        players.append(p)


    team = Team(players)
    

if __name__ == "__main__":
    main()