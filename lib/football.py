class FootballGame:
    def __init__(self, teamA, teamB):
        self.teamA = teamA
        self.teamB = teamB

        self.winner = None

        self.timeRemaining = 3600

        

    def play(self):
        pass
    

    def returnWinner(self):
        if (self.winner == None):
            print("No winner - game in progress")
        else:
            print(self.winner)
        return self.winner