import platform as pf
from time import sleep
import os 

# ===========
# Classes
# ===========

class screen:
    def __init__(self, contents: list[str]):
        self.contents = contents 
    
    @property
    def contents(self):
        return self.__contents;
    
    @contents.setter
    def contents(self, new_contents: list):
        self.__contents = new_contents
        self.update()
        return self.contents;
    
    def __add__(self, other: str):
        self.contents.append(other)
        return self.contents;
    
    def update(self):
        clear()
        for line in self.contents:
            print(line)
    
    def clear(self):
        clear()
        self.contents = []
    
    def slow_clear(self):
        build = ""
        for line in self.contents:
            build += f"{line}\n"
        build_edit = build
        for x in range(len(build)):
            build_edit = build_edit[:-1]
            clear()
            print(build_edit)
            sleep(0.01)
        self.clear()

# ===========
# Functions
# ===========

def clear(screen: screen = None):
    # Check if the platform is windows
    if pf.system() == "Windows":
        # If so, run window's "cls" command
        os.system("cls")
    else:
        # If not, run the linux "clear" command
        os.system("clear")
    if screen:
        screen.clear()

def typed(text: str, time_between: float = 0.02, /, screen: screen = None):
    for i in text:
        print(i, end="", flush="false")
        sleep(time_between)
    sleep(time_between*3)
    if screen:
        screen += text
    print()