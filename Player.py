from Territory import Territory
#from Land import Land
import numpy as np

class Player:

    def __init__(self, inName, inColor, inArmy = 40):
        self.army = inArmy
        self.name = inName
        self.color = inColor
        self.territoriesCount = 0

    def __str__(self):
        # print(self.name)
        return(self.name)
    
    def show_player(self, land):
        terrList = ""
        owned_terr = self.ownedTerrList(land)
        for i in range(len(owned_terr)):
            terrList += " | " + str(land.get_territories()[owned_terr[i][0]])
        print(self.color, "'s territories are :", terrList, '\n')
    
    def get_army(self):
        return self.army

    def get_color(self):
        return self.color
    
    def get_territoriesCount(self):
        return self.territoriesCount
    
    def set_army(self, inArmy):
        self.army = inArmy
    
    def set_territoriesCount(self, inCount):
        self.territoriesCount = inCount
    
    def assign(self, terr):
        if terr.get_ownership() == None:
            self.set_territoriesCount(self.get_territoriesCount() + 1)
            terr.set_ownership(self)
        terr.set_army(terr.get_army() + 1)
    
    def ownedTerrList(self, land):
        owned = []
        for i in range(land.get_nbTerritories()):
            terr = land.get_territories()[i]
            if terr.get_ownership() == self:
                owned.append([i, terr.get_name()])
        return owned
    
    def attack(self, terr1, terr2, till_end = True):
        if terr2.ownership == self:
            print("You already own this territory", '\n', "Can't attack")
        elif terr1.army < 2:
            print("Too few soldiers on this territory.", '\n', "Can't attack")
        else:
            battle = self._battle(terr1.get_army(), terr2.get_army(), till_end)
            terr2.get_ownership().set_army(terr2.get_ownership().get_army() - battle[4])
            self.set_army(self.get_army() - battle[3])
            print("Battle finished")
            if battle[0]:
                terr2.get_ownership().set_territoriesCount(terr2.get_ownership().get_territoriesCount() - 1)
                terr2.set_ownership(self)
                self.set_territoriesCount(self.get_territoriesCount() + 1)
                print(self.get_color(), "took ownership of", terr2.get_name(), "loosing", battle[3], "soldiers.")
            else:
                print("The defender held his position loosing", battle[4], "soldiers.")
        
            
    
    def _battle(self, attacker, defender, till_end):
        aLoss = 0
        dLoss = 0
        if till_end:
            while (attacker >= 2) and (defender >= 1):
                aDice1 = np.random.randint(1,6)
                aDice2 = np.random.randint(1,6)
                aDice3 = np.random.randint(1,6)
                dDice1 = np.random.randint(1,6)
                dDice2 = np.random.randint(1,6)
                if attacker > 3:
                    aDices = [aDice1, aDice2, aDice3]
                elif attacker == 3:
                    aDices = [aDice1, aDice2]
                else:
                    aDices = [aDice1]
                if defender >= 2:
                    dDices = [dDice1, dDice2]
                else:
                    dDices = [dDice1]
                aDices.sort()
                dDices.sort()

                for d in range(min(len(dDices),len(aDices))):
                    if dDices[d] >= aDices[d]:
                        attacker -= 1
                        aLoss += 1
                    else:
                        defender -=1
                        dLoss += 1
            if defender == 0:
                return [True, attacker, defender, aLoss, dLoss]
            else:
                return [False, attacker, defender, aLoss, dLoss]
        else:
            aDice1 = np.random.randint(1,6)
            aDice2 = np.random.randint(1,6)
            aDice3 = np.random.randint(1,6)
            dDice1 = np.random.randint(1,6)
            dDice2 = np.random.randint(1,6)
            if attacker > 3:
                aDices = [aDice1, aDice2, aDice3]
            elif attacker == 3:
                aDices = [aDice1, aDice2]
            else:
                aDices = [aDice1]
            if defender >= 2:
                dDices = [dDice1, dDice2]
            else:
                dDices = [dDice1]
            aDices.sort()
            dDices.sort()

            for d in range(min(len(dDices),len(aDices))):
                if dDices[d] >= aDices[d]:
                    attacker -= 1
                    aLoss += 1
                else:
                    defender -=1
                    dLoss += 1
            if defender == 0:
                return [True, attacker, defender, aLoss, dLoss]
            else:
                return [False, attacker, defender, aLoss, dLoss]
    