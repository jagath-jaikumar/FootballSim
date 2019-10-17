class Player:
    def __init__(self, stats):
        self.stats = stats
        self.name = stats['Name']
        self.team = stats['Team']
        self.position = stats['Position']
        self.ovr = stats['OVR']
    
    # @property
    # def name():
    #     return self.name
    
    # @property
    # def team():
    #     return self.team
    
    # @property
    # def position():
    #     return self.position
    
    # @property
    # def ovr():
    #     return self.ovr