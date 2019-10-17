from lib.player import Player
from lib.team import Team 
from lib.football import FootballGame
from src.generateTeam import getTeam

import numpy as np


def main():
    teamA = getTeam(verbose = False)
    teamB = getTeam(verbose = False)

    f = FootballGame(teamA, teamB)

    f.play()

    f.returnWinner()



if __name__ == "__main__":
    main()