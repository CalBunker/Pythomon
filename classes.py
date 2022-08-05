class pokemon:
    def __init__(self, /, name: str = "", moveset: list = [], lvl: int = 0, hp: int = 0, atk: int = 0, spatk: int = 0, defe: int = 0, spdef: int = 0, spd: int = 0):
        self.__name = name
        self.__moveset = moveset
        self.__lvl = lvl
        self.__hp = hp
        self.__atk = atk
        self.__spatk = spatk
        self.__def = defe
        self.__spdef = spdef
        self.__spd = spd
    def __str__(self):
        return str(self.__name)+"\nMoves: "+str(self.__moveset[0])+", "+str(self.__moveset[1])+", "+str(self.__moveset[2])+", "+str(self.__moveset[3])+"\nLevel: "+str(self.__lvl)+"\nHP: "+str(self.__hp)+"\nAttack: "+str(self.__atk)+"\nSpecial Attack: "+str(self.__spatk)+"\nDefense: "+str(self.__def)+"\nSpecial Defense: "+str(self.__spdef)+"\nSpeed: "+str(self.__spd)
    def setName(self, name):
        self.__name = name
    def setMoves(self, move):
        self.__moveset.append(move)
    def setLevel(self, lvl):
        self.__lvl = lvl
    def setHP(self, hp):
        self.__hp = hp
    def setAttack(self, atk):
        self.__atk = atk
    def setSpAttack(self, spatk):
        self.__spatk = spatk
    def setDefense(self, defe):
        self.__def = defe
    def setSpDefense(self, spdef):
        self.__spdef = spdef
    def setSpeed(self, spd):
        self.__spd = spd
    def getName(self):
        return self.__name
    def getMoves(self):
        return self.__moveset
    def getLevel(self):
        return self.__lvl
    def getHP(self):
        return self.__hp
    def getAttack(self):
        return self.__atk
    def getSpAttack(self):
        return self.__spatk
    def getDefense(self):
        return self.__def
    def getSpDefense(self):
        return self.__spdef
    def getSpeed(self):
        return self.__spd


class move:
    def __init__(self, /, name: str = "", power: int = 0, pp: int = 0, type: str = "", cat: str = ""):
        self.__name = name
        self.__power = power
        self.__pp = pp
        self.__type = type
        self.__cat = cat
    def __str__(self):
        return str(self.__name)
        #return "This move has "+str(self.__power)+" power\n"+str(self.__pp)+" power points \nIt is "+str(self.__type)+" type\n"+"It is a "+str(self.__cat)+" move"
    def setName(self, name):
        self.__name = name
    def setPower(self, power):
        self.__power = power
    def setPP(self, pp):
        self.__pp = pp
    def setType(self, type):
        self.__type = type
    def setCat(self, cat):
        self.__cat = cat
    def getName(self):
        return self.__name
    def getPower(self):
        return self.__power
    def getPP(self):
        return self.__pp
    def getType(self):
        return self.__type
    def getCat(self):
        return self.__cat