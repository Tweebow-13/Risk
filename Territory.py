class Territory:

    def __init__(self, inName, inCoord = [0,0]):
        self.name = inName
        self.army = 0
        self.ownership = None
        self.x = inCoord[0]
        self.y = inCoord[1]
    
    def __str__(self):
        return(str(self.name) + " : " + str(self.army) + " units")
    
    def get_name(self):
        return self.name
    
    def get_army(self):
        return self.army
    
    def get_ownership(self):
        return self.ownership
    
    def set_army(self, inArmy):
        self.army = inArmy
    
    def set_ownership(self, inOwnership):
        self.ownership = inOwnership