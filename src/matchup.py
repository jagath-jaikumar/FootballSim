from lib.player import Player
from lib.team import Team 
from src.generateTeam import getTeam


def main():
    teamA = getTeam(verbose = False)
    teamB = getTeam(verbose = False)

    if teamA.ovr > teamB.ovr:
        print(teamA.name + " Wins!")
    else:
        print(teamB.name + " Wins!")



if __name__ == "__main__":
    main()