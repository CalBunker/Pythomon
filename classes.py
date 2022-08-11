from enum import Enum
import colorama as c

# =============================================================================
# ENTITY SYSTEM
# =============================================================================

class entity:
    '''
    General entity. From pokemon to player to trainer. It is 
    not recommended to use this class directly.
    '''
    # Require name, make color optional and require a colorama Fore color
    def __init__(self, name: str, /, color: c.Fore = c.Fore.WHITE):
        self.__name = name 
        self.color = color
    
    # Creates getter variable for name (usage: self.name)
    @property
    def name(self):
        return self.__name

    # Allows for printing of entity name with color and text
    def speak(self, text):
        # Print name with color
        print(f"{self.color}{self.name}")
        # Print decoratory dashes
        print(f'{"-"*len(self.name)}\n')
        # Print text with color and reset color
        print(f"{text} {c.Fore.RESET}")

# =============================================================================
# POKEMON SYSTEM
# =============================================================================
    
class pokemon_type(Enum):
    '''
    Enum for pokemon/move types.
    '''
    NORMAL = 0
    FIRE = 1
    WATER = 2
    ELECTRIC = 3
    GRASS = 4
    ICE = 5
    FIGHTING = 6
    POISON = 7
    GROUND = 8
    FLYING = 9
    PSYCHIC = 10
    BUG = 11
    ROCK = 12
    GHOST = 13
    DRAGON = 14
    DARK = 15
    STEEL = 16
    FAIRY = 17

class category(Enum):
    '''
    Enum for categories pokemon moves.
    '''
    PHYSICAL = 0
    SPECIAL = 1
    STATUS = 2

class move:
    '''
    Class to define pokemon moves. Often used as parameters for
    creating pokemon.
    '''
    def __init__(self, name: str, power: int, pp: int, type: pokemon_type, cat: category):
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

class pokemon(entity):
    '''
    Class for Pokemon. Allows you to create a pokemon, and define a moveset.
    '''
    def __init__(self, name: str, moveset: list[move], lvl: int, hp: int, atk: int, spatk: int, defe: int, spdef: int, spd: int, /, color: c.Fore = c.Fore.WHITE):
        # Send parameters to super class (the entity class in this case)
        super().__init__(name, color)
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

# =============================================================================
# INTERACTABLE NPC SYSTEM
# =============================================================================

class npc(entity):
    pass 

class trainer(entity):
    pass

# =============================================================================
# INVENTORY SYSTEM
# =============================================================================
class item:
    '''
    Items are used to heal pokemon and to boost stats.
    '''
    def __init__(self, name: str, heal: int, boost: int):
        self.name = name
        self.heal = heal
        self.boost = boost

class backpack:
    '''
    The backpack is a list of pokemon and items, with a system
    for adding and removing pokemon and items.
    '''
    def __init__(self, /, contents: list[pokemon, item] = []):
        self.contents = contents
    
    # Creates a get property for contents in the backpack.
    @property
    def contents(self):
        # Returns the private contents variable.
        return self.__contents
    
    # Creates a set property for contents in the backpack.
    @contents.setter
    def contents(self, new_contents: list):
        # Sets the private contents variable to the new contents.
        self.__contents = new_contents
        # Returns the new contents.
        return self.contents;
    
    # Adds a pokemon/item to the backpack 
    # (this allows this kind of syntax: "backpack += pokemon or item")
    def __add__(self, other: pokemon | item):
        # Append "other" to contents.
        self.contents.append(other)
        # Returns the new contents.
        return self.contents;

# =============================================================================
# PLAYER SYSTEM
# =============================================================================

class player(entity):
    '''
    Class for the player. Allows you to create a player,
    define a backpack to be attatched to the player, and
    define a color for the player.
    '''
    def __init__(self, name: str = "undefined", backpackobj: backpack = backpack(), /, color: c.Fore = c.Fore.WHITE):
        # Pass parameters to the superclass.
        super().__init__(name, color)
        self.backpack = backpackobj