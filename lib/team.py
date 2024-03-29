import numpy as np


class Team:
    def __init__(self, name, players):
        self.name = name


        self.startingRoster = {}
        self.startingRosterSpots = {}

        self.schema = None

        self.startingRosterSpots["QB"] = 1
        self.startingRosterSpots["FB"] = 1
        self.startingRosterSpots["HB"] = 1
        self.startingRosterSpots["WR"] = 3
        self.startingRosterSpots["TE"] = 1
        self.startingRosterSpots["LT"] = 1
        self.startingRosterSpots["LG"] = 1
        self.startingRosterSpots["C"] = 1
        self.startingRosterSpots["RG"] = 1
        self.startingRosterSpots["RT"] = 1

        self.startingRosterSpots["LE"] = 1
        self.startingRosterSpots["RE"] = 1
        self.startingRosterSpots["DT"] = 1
        self.startingRosterSpots["LOLB"] = 1
        self.startingRosterSpots["MLB"] = 1
        self.startingRosterSpots["ROLB"] = 1
        self.startingRosterSpots["CB"] = 2
        self.startingRosterSpots["SS"] = 1
        self.startingRosterSpots["FS"] = 1

        self.startingRosterSpots["K"] = 1
        self.startingRosterSpots["P"] = 1
        self.startingRosterSpots["LS"] = 1

        self.offense = ['QB', 'HB', 'FB', 'WR', 'TE', 'LT', 'LG', 'C','RG','RT']
        self.defense = ['LE', 'RE', 'DT', 'LOLB', 'MLB', 'ROLB', 'CB', 'SS', 'FS']

        self.runOffense = ['HB', 'FB', 'LT', 'LG', 'C', 'RG', 'RT']
        self.passOffense = ['QB', 'WR','TE', 'LT', 'LG', 'C', 'RG', 'RT']
        self.offensiveline = ['LT','LG','C','RG','RT']
        self.runDefense = ['LE','RE','DT','LOLB','ROLB','MLB']
        self.passDefense = ['LOLB','ROLB','CB','SS','FS']

        self.specialTeams = ['K','P','LS']

        self.offovr = 0
        self.defovr = 0
        self.stovr = 0
        self.ovr = 0

        self.players = {}

        for p in players:
            if p.stats["Position"] in self.players:
                self.players[p.stats["Position"]].append(p)   
            else:
                self.players[p.stats["Position"]] = [p]
                
        

        for pos in self.players:
            l = self.players[pos]
            l.sort(key=lambda x: x.ovr, reverse = True)
            self.players[pos] = l 
        

        for pos in self.players:
            n = self.startingRosterSpots[str(pos)]
            for i in range(n):
                if pos in self.startingRoster:
                    self.startingRoster[pos].append(self.players[pos][i])
                else:
                    self.startingRoster[pos] = [self.players[pos][i]]
        
        self.o = []
        self.d = []
        self.st = []
        self.runO = []
        self.passO = []
        self.runD = []
        self.passD = []
        self.oline = []


        for pos in self.startingRoster:
            l = self.startingRoster[pos]
            if pos in self.offense:
                for i in l:
                    self.o.append(i)
            if pos in self.defense:
                for i in l:
                    self.d.append(i)
            if pos in self.specialTeams:
                for i in l:
                    self.st.append(i)
            if pos in self.runOffense:
                for i in l:
                    self.runO.append(i)
            if pos in self.passOffense:
                for i in l:
                    self.passO.append(i)
            if pos in self.runDefense:
                for i in l:
                    self.runD.append(i)
            if pos in self.passDefense:
                for i in l:
                    self.passD.append(i)
            if pos in self.offensiveline:
                for i in l:
                    self.oline.append(i)
        
        self.offovr = np.around(np.mean([x.ovr for x in self.o]))
        self.defovr = np.around(np.mean([x.ovr for x in self.d]))
        self.stovr = np.around(np.mean([x.ovr for x in self.st]))

        self.runovr = np.around(np.mean([x.ovr for x in self.runO]))
        self.passovr = np.around(np.mean([x.ovr for x in self.passO]))
        self.rundef = np.around(np.mean([x.ovr for x in self.runD]))
        self.passdef = np.around(np.mean([x.ovr for x in self.passD]))
        self.olineovr = np.around(np.mean([x.ovr for x in self.oline]))

        self.ovr = np.around(.4 * self.offovr + .4 * self.defovr + .2 * self.stovr, 0) 



        self.run_pass_ratio = 1.0 * self.runovr / self.passovr

        self.run_pass_defense = 1.0 * self.rundef / self.passdef

    def printStats(self):
        print("STATS: ")
        print("Total Overall: " + str(self.ovr))
        print("Offense:  " + str(self.offovr))
        print("Defense: " + str(self.defovr))
        print("Special Teams: " + str(self.stovr))


    def printLineup(self):
        print("LINEUP: ")
        for pos in self.offense:
            l = self.startingRoster[pos]
            print(pos)
            print([x.name for x in l])

        for pos in self.defense:
            l = self.startingRoster[pos]
            print(pos)
            print([x.name for x in l])
                
        