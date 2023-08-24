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
        self.job = ""                   # player class type
        self.location = "c4"
        self.gameover = False
myPlayer = player()

##### TITLE SELECTIONS #####

def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game()                    # placeholder until code is written
    elif option.lower() == ("help"):
        help_menu()                     # help menu
    elif option.lower() == ("quit"):
        sys.exit()                      # system exit game

    while option.lower() not in ["play", "help", "quit"]:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
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
RIGHT = "right", "east"

solved_places = {"a1": False, "b1": False, "c1": False, "d1": False, "e1": False,
                 "a2": False, "b2": False, "c2": False, "d2": False, "e2": False,
                 "a3": False, "b3": False, "c3": False, "d3": False, "e3": False,
                 "a4": False, "b4": False, "c4": False, "d4": False, "e4": False,
                 "a5": False, "b5": False, "c5": False, "d5": False, "e5": False,
                 "a6": False, "b6": False, "c6": False, "d6": False, "e6": False,
                 "a7": False, "b7": False, "c7": False, "d7": False, "e7": False,
                 }

zonemap = {
    "a1": {
        "ZONENAME": "WASTELANDa1",
        "DESCRIPTION": "It's strange, this land before you. There is no life, nothing to see, just wasteland...",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": "",
        "DOWN": "a2",
        "LEFT": "",
        "RIGHT": "b1",
    },
    "b1": {
        "ZONENAME": "SEAb1",
        "DESCRIPTION": "You're standing on the northern shore of the island, there are no boats or bridges.",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": "",
        "DOWN": "b2",
        "LEFT": "a1",
        "RIGHT": "c1",
    },
    "c1": {
        "ZONENAME": "SEAc1",
        "DESCRIPTION": "You're standing on the northern shore of the island, there are no boats or bridges.",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": "",
        "DOWN": "c2",
        "LEFT": "b1",
        "RIGHT": "d1",
    },
    "d1": {
        "ZONENAME": "SEAd1",
        "DESCRIPTION": "You're standing on the northern shore of the island, there are no boats or bridges.",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": "",
        "DOWN": "d2",
        "LEFT": "c1",
        "RIGHT": "e1",
    },
    "e1": {
        "ZONENAME": "WASTELANDe1",
        "DESCRIPTION": "It's strange, this land before you. There is no life, nothing to see, just wasteland...",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": "",
        "DOWN": "e2",
        "LEFT": "d1",
        "RIGHT": "",
    },
    "a2": {
        "ZONENAME": "SEAa2",
        "DESCRIPTION": "You're standing on the western shore of the island, there are no boats or bridges.",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": "a1",
        "DOWN": "a3",
        "LEFT": "",
        "RIGHT": "b2",
    },
    "b2": {
        "ZONENAME": "NORTH WEST DESSERT",
        "DESCRIPTION": "The ground shakes, as if something is under there. Sand spans as far as the eye can see, the odd cactus here and there.",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": "b1",
        "DOWN": "b3",
        "LEFT": "a2",
        "RIGHT": "c2",
    },
    "c2": {
        "ZONENAME": "NORTH DESSERT",
        "DESCRIPTION": "Tiny mounds dot the sandy landscape, a thunderous sound of millions of tiny feet marching in unison is getting louder, as if coming from below the surface...",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": "c1",
        "DOWN": "c3",
        "LEFT": "b2",
        "RIGHT": "d2",
    },
    "d2": {
        "ZONENAME": "NORTH EAST DESSERT",
        "DESCRIPTION": "A cool breeze feels refreshing, and something glimmers and twinkles, surrounded by palm tress",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": "d1",
        "DOWN": "d3",
        "LEFT": "c2",
        "RIGHT": "e2",
    },
    "e2": {
        "ZONENAME": "SEAe2",
        "DESCRIPTION": "You're standing on the eastern shore of the island, there are no boats or bridges.",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": "e1",
        "DOWN": "e3",
        "LEFT": "c2",
        "RIGHT": "",
    },
    "a3": {
        "ZONENAME": "SEAa3",
        "DESCRIPTION": "You're standing on the western shore of the island, there are no boats or bridges.",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": "a2",
        "DOWN": "a4",
        "LEFT": "",
        "RIGHT": "b3",
    },
    "b3": {
        "ZONENAME": "NORTH WEST FORREST",
        "DESCRIPTION": "This unexplored forrest may contain some mystery in the future, but for now it's just a forrest",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": "b2",
        "DOWN": "b4",
        "LEFT": "a3",
        "RIGHT": "c3",
    },
    "c3": {
        "ZONENAME": "FARMLANDS",
        "DESCRIPTION": "Local Farmers tend to their crops, and a scare crow stands silently in the field",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": "c2",
        "DOWN": "c4",
        "LEFT": "b3",
        "RIGHT": "d3",
    },
    "d3": {
        "ZONENAME": "NORTH EAST FORREST",
        "DESCRIPTION": "This unexplored forrest may contain some mystery in the future, but for now it's just a forrest",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": "d2",
        "DOWN": "d4",
        "LEFT": "c3",
        "RIGHT": "e3",
    },
    "e3": {
        "ZONENAME": "SEAe3",
        "DESCRIPTION": "You're standing on the eastern shore of the island, there are no boats or bridges.",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": "d2",
        "DOWN": "d4",
        "LEFT": "c3",
        "RIGHT": "e3",
    },
    "a4": {
        "ZONENAME": "WEST BEACH",
        "DESCRIPTION": "This sandy beach on the western shore of Lithuin Island is great for getting a tan",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": "a3",
        "DOWN": "a5",
        "LEFT": "",
        "RIGHT": "b4",
    },
    "b4": {
        "ZONENAME": "PLAINS",
        "DESCRIPTION": "Gentle hills, fields of grass, and the occasional horse are all that can be seen here",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": "b3",
        "DOWN": "b5",
        "LEFT": "a4",
        "RIGHT": "c4",
    },
    "c4": {
        "ZONENAME": "CENTRAL FORREST",
        "DESCRIPTION": "The Central Forrest is in the middle of the Island of Lithuin. Tall tress create a canopy that blocks the sky, but causes the forrest floor to glisten with a green, almost magical glow. A strange mound of dirt a few steps away appears fairly fresh.",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": "c3",
        "DOWN": "c5",
        "LEFT": "b4",
        "RIGHT": "d4",
    },
    "d4": {
        "ZONENAME": "CAVE",
        "DESCRIPTION": "This cave is dark, and smelly, but goes deep...",
        "EXAMINATION": "examine",
        "UP": "d3",
        "DOWN": "d5",
        "LEFT": "c4",
        "RIGHT": "e4",
    },
    "e4": {
        "ZONENAME": "WASTELANDe4",
        "DESCRIPTION": "Nothing...a landscape of dust and more dust. No point going any further east...",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": "e3",
        "DOWN": "e5",
        "LEFT": "d4",
        "RIGHT": "",
    },
    "a5": {
        "ZONENAME": "SEAa5",
        "DESCRIPTION": "You're standing on the western shore of the island, there are no boats or bridges.",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": "a4",
        "DOWN": "a6",
        "LEFT": "",
        "RIGHT": "b5",
    },
    "b5": {
        "ZONENAME": "HORIZON MOUNTAIN",
        "DESCRIPTION": "A snow-capped peak that seems to touch the sky, and a treacherous climb...",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": "b4",
        "DOWN": "b6",
        "LEFT": "a5",
        "RIGHT": "c5",
    },
    "c5": {
        "ZONENAME": "LUMBER TOWN",
        "DESCRIPTION": "The biggest settlement on the Island, but a low population nonetheless",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": "c4",
        "DOWN": "c6",
        "LEFT": "b5",
        "RIGHT": "d5",
    },
    "d5": {
        "ZONENAME": "GOURDA CASTLE",
        "DESCRIPTION": "Named after the singing lady who built it, not much else is known about Gourda Castle, no one has been in there for decades...",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": "d4",
        "DOWN": "d6",
        "LEFT": "c5",
        "RIGHT": "e5",
    },
    "e5": {
        "ZONENAME": "SEAe5",
        "DESCRIPTION": "You're standing on the eastern shore of the island, there are no boats or bridges.",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": "e4",
        "DOWN": "e6",
        "LEFT": "d5",
        "RIGHT": "",
    },
    "a6": {
        "ZONENAME": "SEAa6",
        "DESCRIPTION": "You're standing on the western shore of the island, there are no boats or bridges.",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": "a5",
        "DOWN": "a7",
        "LEFT": "",
        "RIGHT": "b6",
    },
    "b6": {
        "ZONENAME": "LIGHTHOUSE",
        "DESCRIPTION": "A tall, red and white striped lighthouse looks over the sea. The door requires a key",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": "b5",
        "DOWN": "b7",
        "LEFT": "a6",
        "RIGHT": "c6",
    },
    "c6": {
        "ZONENAME": "SWAMP",
        "DESCRIPTION": "A green, thick water covers the floor motionlessly, mangrove trees erupt from the silence",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": "c5",
        "DOWN": "c7",
        "LEFT": "b6",
        "RIGHT": "d6",
    },
    "d6": {
        "ZONENAME": "SOUTH EAST BEACH",
        "DESCRIPTION": "This beach is rocky, Gourda Castle looms over it, and bones remain from unlucky travellers",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": "d5",
        "DOWN": "d7",
        "LEFT": "c6",
        "RIGHT": "e6",
    },
    "e6": {
        "ZONENAME": "SEAe6",
        "DESCRIPTION": "You're standing on the eastern shore of the island, there are no boats or bridges.",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": "e5",
        "DOWN": "e7",
        "LEFT": "d6",
        "RIGHT": "",
    },
    "a7": {
        "ZONENAME": "WASTELANDa7",
        "DESCRIPTION": "Desolate wasteland stretches as far as the eye can see. Theres nowhere to go to the south, or the west",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": "a6",
        "DOWN": "",
        "LEFT": "",
        "RIGHT": "b7",
    },
    "b7": {
        "ZONENAME": "",
        "DESCRIPTION": "You're standing on the southern shore of the island, there are no boats or bridges.",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": ["up", "north"],
        "DOWN": ["down", "south"],
        "LEFT": ["left", "west"],
        "RIGHT": ["right", "east"],
    },
    "c7": {
        "ZONENAME": "",
        "DESCRIPTION": "You're standing on the southern shore of the island, there are no boats or bridges.",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": ["up", "north"],
        "DOWN": ["down", "south"],
        "LEFT": ["left", "west"],
        "RIGHT": ["right", "east"],
    },
    "d7": {
        "ZONENAME": "",
        "DESCRIPTION": "You're standing on the southern shore of the island, there are no boats or bridges.",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": ["up", "north"],
        "DOWN": ["down", "south"],
        "LEFT": ["left", "west"],
        "RIGHT": ["right", "east"],
    },
    "e7": {
        "ZONENAME": "",
        "DESCRIPTION": "description",
        "EXAMINATION": "examine",
        "SOLVED": False,
        "UP": ["up", "north"],
        "DOWN": ["down", "south"],
        "LEFT": ["left", "west"],
        "RIGHT": ["right", "east"],
    }
}



## GAME INTERACTIVITY ##
def print_location():
    print("\n" + ("#" x (4 + len(myPlayer.location))))
    print("# " + myPlayer.location.upper() + " #")
    print("# " + zonemap[myPlayer.location][DESCRIPTION] + " #")
    print("\n" + ("#" x (4 + len(myPlayer.location))))

def prompt():
    print("\n" + "==================")
    print("What would you like to do?")
    action = input("> ")
    acceptable_movement_actions = ["move", "go", "travel", "walk", "journey", "run"]
    acceptable_examine_actions = ["inspect", "examine", "look", "peek", "interact"]
    while action.lower() not in acceptable_examine_actions or action.lower() not in acceptable_examine_actions:
        print("Unknown action, please try again \n")
        action = input("> ")
    if action.lower() == "quit":
        sys.exit()
    elif action.lower() in acceptable_movement_actions:
        player_move(action.lower())
    elif action.lower() in acceptable_examine_actions:
        player_examine(action.lower())

def player_move(myAction):
    ask = "Where would you like to move to?\n"
    dest = input(ask)
    if dest in ["up", "north"]:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    if dest in ["left", "west"]:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    if dest in ["right", "east"]:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)
    if dest in ["down", "south"]:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)
def movement_handler(destination):
    print("\n" + "You have moved to the " + destination + ".")
        myPlayer.location = destination
        print_location()
def player_examine(action):
    if zonemap[myPlayer.location][SOLVED]:
        print("You have already completed this part of the Island.")
    else:
        print("Looks like there's something you need to do here...")





## GAME FUNCTIONALITY ##



def main_game_loop():
    while myPlayer.gameover is False:
        prompt()
        # here handle puzzles, boss, enemies etc

def start_game():
        os.system("clear")

    ## NAME COLLECTION ###
    question1 = "NAME?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name

    ## PLAYER CLASS COLLECTION ##

    question2 = "CLASS?\n"
    valid_jobs = ["warrior", "mage", "priest"]
    question2added = ("You can play as any of the following: " + valid_jobs)
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    player_job = input("> ")

    if myPlayer.job.lower() in valid_jobs:
        myPlayer.job = player_job
        print("You will be known on Lithuin Island as " + myPlayer.name + " the " + myPlayer.job "!\n")
    while myPlayer.job.lower() not in valid_jobs:
        print("That's not a valid player class, try again")
        player_jobs = input("> ")
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print("You are now " + myPlayer.name + " the " + myPlayer.job)

        ## PLAYER STATS ##

        if myPlayer.job is "warrior":
            self.hp = 120
            self.mp = 20
        elif myPlayer.job is "mage":
            self.hp = 20
            self.mp = 120
        elif myPlayer.job is "priest":
            self.hp = 70
            self.mp = 70








## GAME HANDLING ##


