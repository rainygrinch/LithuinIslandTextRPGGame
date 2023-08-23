import random
import time
import os
import sys
import cmd
import textwrap

screen_width = 100

##### PLAYER SETUP #####
class player:
    def __init__(self):
        self.name = ""                  # player name
        self.hp = 0                     # health points
        self.mp = 0                     # magic points
        self.status_effect = []         # status effects
    myPlayer = player()

##### TITLE SELECTIONS #####

def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play")
        start_game()                    # placeholder until code is written
    elif option.lower() == ("help"):
        help_menu()                     # help menu
    elif option.lower() == ("quit"):
        sys.exit()                      # system exit game

    while option.lower() not in ["play", "help", "quit"]:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play")
            start_game()                # placeholder until code is written (second attempt)
        elif option.lower() == ("help"):
            help_menu()                 # help menu (second attempt)
        elif option.lower() == ("quit"):
            sys.exit()                  # system exit game (second attempt)


## TITLE SCREEN ##
def title_screen():
    os.system("clear")
    print("#############################")
    print("# Welcome to Lithuin Island #")
    print("#############################")
    print("#         - Play -          #")
    print("#         - Help -          #")
    print("#         - Quit -          #")
    print("#############################")
    print("# Game Design - RainyGrinch #")
    print("#  Inspired by - BTONG.ME   #")
    print("#############################")
    title_screen_selections()

## HELP MENU ##
def help_menu():
    print("#############################")
    print("# Welcome to Lithuin Island #")
    print("#############################")
    print("# Use up, down, left, right #")
    print("#   to move about the map   #")
    print("# type commands into the    #")
    print("# prompt to perform actions #")
    print("#   Use 'look' to inspect   #")
    print("# Good luck, and have fun   #")
    print("#############################")


## GAME FUNCTIONALITY ##
def start_game():




## MAP ##
"""
  A   B   C   D   E
+---+---+---+---+---+
|   |   |   |   |   |   1
+---+---+---+---+---+
|   |   |   |   |   |   2
+---+---+---+---+---+
|   |   |   |   |   |   3
+---+---+---+---+---+
|   |   |   |   |   |   4
+---+---+---+---+---+
|   |   |   |   |   |   5
+---+---+---+---+---+
|   |   |   |   |   |   6
+---+---+---+---+---+
|   |   |   |   |   |   7
+---+---+---+---+---+
"""

ZONENAME = ""
DESCRIPTION = "description"
EXAMINATION = "examine"
SOLVED = False
UP = "up", "north"
DOWN = "down", "south"
LEFT = "left", "west"
RIGHT - "right", "east"

solved_places = {"a1": False, "b1": False, "c1": False, "d1": False, "e1": False
                 "a2": False, "b2": False, "c2": False, "d2": False, "e2": False
                 "a3": False, "b3": False, "c3": False, "d3": False, "e3": False
                 "a4": False, "b4": False, "c4": False, "d4": False, "e4": False
                 "a5": False, "b5": False, "c5": False, "d5": False, "e5": False
                 "a6": False, "b6": False, "c6": False, "d6": False, "e6": False
                 "a7": False, "b7": False, "c7": False, "d7": False, "e7": False
                 }