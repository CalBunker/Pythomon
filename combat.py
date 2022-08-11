import platform as pf
import colorama as c
import random as r
import time as t
import os

# Good on you for importing only necessary modules!
from classes import pokemon

def clear():
    # Check if the platform is windows
    if pf.system() == "Windows":
        # If so, run window's "cls" command
        os.system("cls")
    else:
        # If not, run the linux "clear" command
        os.system("clear")

def typed(text: str, time_between: float = 0.02):
    for i in text:
        print(i, end="", flush="false")
        t.sleep(time_between)
    t.sleep(time_between*3)
    print()

def fight(pk1: pokemon, pk2: pokemon):
    name1 = pk1.name
    moves1 = pk1.getMoves()
    hp1 = pk1.getHP()
    atk1 = pk1.getAttack()
    spatk1 = pk1.getSpAttack()
    def1 = pk1.getDefense()
    spdef1 = pk1.getSpDefense()
    spd1 = pk1.getSpeed()
    name2 = pk2.name
    moves2 = pk1.getMoves()
    hp2 = pk2.getHP()
    atk2 = pk2.getAttack()
    spatk2 = pk2.getSpAttack()
    def2 = pk2.getDefense()
    spdef2 = pk2.getSpDefense()
    spd2 = pk2.getSpeed()
    if hp1 > 0:
        if hp2 > 0:
            choice1 = 1
            choice2 = 1
            hpbar1 = hp1/5
            hpbar2 = hp2/5
            print(c.Fore.BLUE)
            typed(str(name1))

            print("="*int(hpbar1), end="")

            print(f"\n{c.Fore.RED}")
            typed(str(name2))
            for x in range(int(hpbar2)):
                print("=", end="")
            print(f"\n{c.Fore.WHITE}")
            while choice1 != 3:
                typed("What will "+str(name1)+" do?")
                typed("1 - Attack")
                typed("2 - End Battle")
                choice1 = int(input(""))
                print("")
                if choice1 == 1:
                    typed("1 - "+str(moves1[0]))
                    typed("2 - "+str(moves1[1]))
                    typed("3 - "+str(moves1[2]))
                    typed("4 - "+str(moves1[3]))
                    moveChoice1 = input("")
                    if moveChoice1 == "1":
                        moveChoice1 = moves1[0]
                    elif moveChoice1 == "2":
                        moveChoice1 = moves1[1]
                    elif moveChoice1 == "3":
                        moveChoice1 = moves1[2]
                    elif moveChoice1 == "4":
                        moveChoice1 = moves1[3]
                    print("")
                    while choice2 != 3:
                        typed("What will "+str(name2)+" do?")
                        typed("1 - Attack")
                        typed("2 - End Battle\n")
                        choice2 = int(input(""))
                        if choice2 == 1:
                            typed("1 - "+str(moves2[0]))
                            typed("2 - "+str(moves2[1]))
                            typed("3 - "+str(moves2[2]))
                            typed("4 - "+str(moves2[3]))
                            moveChoice2 = input("")
                            if moveChoice2 == "1":
                                moveChoice2 = moves2[0]
                            elif moveChoice2 == "2":
                                moveChoice2 = moves2[1]
                            elif moveChoice2 == "3":
                                moveChoice2 = moves2[2]
                            elif moveChoice2 == "4":
                                moveChoice2 = moves2[3]
                            print("")
                            choice1 = 3
                            choice2 = 3
                        if choice2 == 2:
                            exit()
                if choice1 == 2:
                    exit()
            if spd2 > spd1:
                # pk2 goes first
                # pk2 attacks
                dmg = atk2 - def1
                hp1 -= dmg
                typed(str(name2)+" used "+str(moveChoice2.getName())+"!")
                typed(str(name1)+" took "+str(moveChoice2.getPower())+" damage!")
                print("")
                if hp1 <= 0:
                    typed(str(name1)+" fainted!")
                    typed(str(name2)+" wins!")
                    exit()
                elif hp1 > 0:
                    typed(str(name1)+" has "+str(hp1)+" HP left!")
                    print("")
                    # pk1 attacks
                    dmg = atk1 - def2
                    hp2 -= dmg
                    typed(str(name1)+" used "+str(moveChoice1.getName())+"!")
                    typed(str(name2)+" took "+str(moveChoice1.getPower())+" damage!")
                    print("")
            else:
                # pk1 goes first
                # pk1 attacks
                dmg = atk1 - def2
                hp2 -= dmg
                typed(str(name1)+" used "+str(moveChoice1.getName())+"!")
                typed(str(name2)+" took "+str(moveChoice1.getPower())+" damage!")
                print("")
                if hp2 <= 0:
                    typed(str(name2)+" fainted!")
                    typed(str(name1)+" won!")
                    exit()
                elif hp2 > 0:
                    typed(str(name2)+" has "+str(hp2)+" HP left!")
                    print("")
                    # pk2 attacks
                    dmg = atk2 - def1
                    hp1 -= dmg
                    typed(str(name2)+" used "+str(moveChoice2.getName())+"!")
                    typed(str(name1)+" took "+str(moveChoice2.getPower())+" damage!")
                    print("")
        else:
            typed(str(name2)+" has fainted!")
            typed("Player 1 won!")
            exit()
    else:
        typed(str(name1)+" has fainted!")
        typed("Player 2 won!")
        exit()