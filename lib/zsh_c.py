from os import system as sc
from os import getcwd, path, chdir, listdir
import logging

from lib.git_c import gitPush
from lib.profile import USR_NAME, ZSH_CUSTOM_PATH, DISPLAYS, PROP_9_TAP, WORKSPACES
from tools.termup import prompt

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

LOOP = True

def aliasup():
    sc("rm -rf {}".format(ZSH_CUSTOM_PATH))

    chdir("/home/{}/Documents/faster-zsh".format(USR_NAME))
    sc("cp ./code_aliases.zsh {}".format(ZSH_CUSTOM_PATH))
    prompt("New alias saved locally. Please use \"src\" to get the changes on your term.")

def aliassave():
    aliasup()
    com = input("commit :")

    sc("git add code_aliases.zsh")
    sc("git commit -m \"{}\"".format(com))
    sc("git push origin master")

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

def forceTapping():

    for prop in PROP_9_TAP:
        sc("xinput set-prop 9 {} 1".format(prop))

def workspace_loader():
    """Load all saved workspaces"""
    for workspace in WORKSPACES:
        prompt("Restoring workspace {}".format(workspace))
        sc("i3-resurrect restore -w {}".format(workspace))

def apt():
    prompt("Welcome to the installer environnement.", type="okblue")

    while LOOP:
        prompt("Name the package you need to install now or quit/ENTER to exit.")
        pkg = input(">")

        if pkg == "" or pkg == "quit":
            prompt("Have a nice coding day.", type="okblue", plus="bold")
            exit()

        else:
            sc("sudo apt-get install {}".format(pkg))

def profile_edit():
    sc("vs ~/Documents/faster-zsh/lib/profile.py")

