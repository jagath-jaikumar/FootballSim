class FootballGame:
    def __init__(self, teamA, teamB):
        self.teamA = teamA
        self.teamB = teamB

        self.winner = None

        self.timeRemaining = 3600



        self.actions = ['run','pass']
        #               <5         <15      >15
        self.runPlay = ['short', 'medium','long']
        #                <5         <20      >20
        self.passPlay = ['short', 'medium','long']


    def play(self):
        pass
    

    def returnWinner(self):
        if (self.winner == None):
            print("No winner - game in progress")
        else:
            print(self.winner)
        return self.winner