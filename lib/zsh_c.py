from os import system as sc
from os import getcwd, path, chdir, listdir
import logging

from lib.git_c import gitPush
from lib.profile import USR_NAME, ZSH_CUSTOM_PATH, PROP_9_TAP
from tools.termup import prompt

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

LOOP = True

def aliasup():
    sc("rm -rf {}".format(ZSH_CUSTOM_PATH))

    chdir("/home/{}/Documents/faster-zsh".format(USR_NAME))
    sc("cp ./code_aliases.zsh {}".format(ZSH_CUSTOM_PATH))
    prompt("New alias saved locally. Please use \"src\" to update your terminal.")

def aliassave():
    aliasup()
    com = input("commit :")

    sc("git add code_aliases.zsh")
    sc("git commit -m \"{}\"".format(com))
    sc("git push origin master")

def forceTapping():

    for prop in PROP_9_TAP:
        sc("xinput set-prop 9 {} 1".format(prop))

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

