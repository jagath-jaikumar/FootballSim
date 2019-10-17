class Player:
    def __init__(self, stats):
        self.stats = stats
        self.name = stats['Name']
        self.team = stats['Team']
        self.position = stats['Position']
        self.ovr = stats['OVR']
    
    def __str__(self):
        return self.name