from lib.profile import WORKSPACES, DISPLAYS
from tools.termup import prompt

from os import system as sc

def workspace_loader():
    """Load all saved workspaces"""
    for workspace in WORKSPACES:
        prompt("Restoring workspace {}".format(workspace))
        sc("i3-resurrect restore -w {}".format(workspace))

def bright(bright_lvl):
    formatted_lvl = None

    if int(bright_lvl) < 10 and int(bright_lvl) > 0:
        formatted_lvl = "0." + bright_lvl
        formatted_lvl = float(formatted_lvl)

    elif int(bright_lvl) == 10:
        formatted_lvl = 1


    if formatted_lvl != None:
        index = 0
        for display in DISPLAYS:
            sc("xrandr --output {} --brightness {}".format(display, formatted_lvl))
            index += 1
        
        prompt("Brightness set to {}".format(bright_lvl))

    elif formatted_lvl == None:
        prompt("ERROR: Invalid arguments.")

def bastion():
    print("Moving this workspace to bastion screen.")
    sc("xrandr --output {} --auto --right-of {}".format(DISPLAYS[1], DISPLAYS[0]))
    sc("i3-msg move workspace to output right")

def scout():
    print("Moving this workspace to scout screen.")
    sc("i3-msg move workspace to output right")
    sc("xrandr --output {} --off".format(DISPLAYS[1]))

def wmove(side):

    if side == "down":
        side = "left"

    elif side == "up":
        side = "right"

    sc("i3-msg move workspace to output " + side)
    prompt("Workspace moved.")